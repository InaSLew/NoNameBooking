import datetime
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['booking_id', 'timestamp']

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        return firstname[0].upper()+firstname[1:].lower()
    
    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        return lastname[0].upper() + lastname[1:].lower()
    
    def clean_title(self):
        title = self.cleaned_data['title']
        return title[0].upper() + title[1:].lower()
    
    def clean_booked_date(self):
        booked_date = self.cleaned_data['booked_date']

        # Check if the date is not in the past
        if booked_date < datetime.date.today():
            raise forms.ValidationError('Date in past', code='invalid')
        
        # Check if the date is within the upcoming month (4 weeks)
        if booked_date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError('Reservation more than 4 weeks ahead', code='invalid')
        
        return booked_date

class DeleteBookingForm(forms.Form):
    email = forms.EmailField()
    booking_id = forms.CharField(max_length=5)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        booking_id = cleaned_data.get('booking_id')

        try:
            # print('Attempting to get query using email')
            target_reservation = Booking.objects.get(email=email)
        except Exception:
            # print('Query does not exist')
            self.add_error('email', forms.ValidationError('No reservation made under this email!', code='invalid'))
            return {'email': email, 'booking_id': booking_id}
        
        if target_reservation.booking_id.hex[:5].upper() != booking_id:
            # print(target_reservation.booking_id.hex[:5].upper())
            self.add_error('booking_id', forms.ValidationError('Invalid booking ID!', code='invalid'))
            return {'email': email, 'booking_id': booking_id}