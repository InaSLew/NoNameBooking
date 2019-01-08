import datetime
from django.db import models
from django.forms import ModelForm, ValidationError

class Booking(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    title = models.CharField(max_length=4)
    phone_number = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)
    booked_date = models.DateField(auto_now=False, auto_now_add=False)
    booked_time = models.CharField(max_length=5)
    guests_number = models.IntegerField(default=0)
    customer_notes = models.TextField(default='lorem ipsum',blank=True)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}.{self.lastname}'s reservation on {self.booked_date} at {self.booked_time}; Contact:{self.phone_number}"

class BookingForm(ModelForm):

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
            # raise ValidationError(_('Date in past'),code='invalid')
            raise ValidationError('Date in past', code='invalid')
        
        # Check if the date is within the upcoming month (4 weeks)
        if booked_date > datetime.date.today() + datetime.timedelta(weeks=4):
            # raise ValidationError(_('Reservation more than 4 weeks ahead'),code='invalid')
            raise ValidationError('Reservation more than 4 weeks ahead', code='invalid')
        
        return booked_date

    class Meta:
        model = Booking
        fields = '__all__'