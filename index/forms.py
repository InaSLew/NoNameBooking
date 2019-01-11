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
        
        if target_reservation.get_booking_id() != booking_id:
            # print(target_reservation.booking_id.hex[:5].upper())
            self.add_error('booking_id', forms.ValidationError('Invalid booking ID for the provided email!', code='invalid'))
            return {'email': email, 'booking_id': booking_id}

class RescheduleBookingForm(forms.Form):
    email = forms.EmailField()
    booking_id = forms.CharField(max_length=5)
    booked_date = forms.DateField(initial=datetime.date.today)
    booked_time = forms.CharField(max_length=5)

    def clean_booked_date(self):
        # print(self.cleaned_data)
        new_booked_date = self.cleaned_data['booked_date']

        # Check if the date is not in the past
        if new_booked_date < datetime.date.today():
            raise forms.ValidationError('Date in past', code='invalid')
        
        # Check if the date is within the upcoming month (4 weeks)
        if new_booked_date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError('Reservation more than 4 weeks ahead', code='invalid')
        
        return new_booked_date


    
    def clean(self):
        cleaned_data = super().clean()
        print(f'Generated from the clean() method: {self.cleaned_data}')
        email = cleaned_data.get('email')
        booking_id = cleaned_data.get('booking_id')
        new_booked_date = cleaned_data.get('booked_date')
        new_booked_time = cleaned_data.get('booked_time')

        try:
            target_reservation = Booking.objects.get(email=email)
        except Exception:
            self.add_error('email', forms.ValidationError('No reservation made under this email!', code='invalid'))
            return {'email': email, 'booking_id': booking_id, 'booked_date': new_booked_date, 'booked_time': new_booked_time}
        
        if target_reservation.get_booking_id() != booking_id:
            self.add_error('booking_id', forms.ValidationError('Invalid booking ID for the provided email!', code='invalid'))
            return {'email': email, 'booking_id': booking_id, 'booked_date': new_booked_date, 'booked_time': new_booked_time}
        
        if target_reservation.booked_date == new_booked_date and target_reservation.booked_time == new_booked_time:
            self.add_error('booked_time', forms.ValidationError('You seem to be rescheduling to the same day and time. Please choose at least a different time.', code='invalid'))
            return {'email': email, 'booking_id': booking_id, 'booked_date': new_booked_date, 'booked_time': new_booked_time}