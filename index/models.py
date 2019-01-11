import uuid
from django.db import models


class Booking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, help_text='A unique id for this particular reservation')
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
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.title}.{self.lastname}'s reservation on {self.booked_date} at {self.booked_time}; Contact:{self.phone_number}; reservation made on: {self.timestamp}"
    
    def get_booking_id(self):
        return self.booking_id.hex[:5].upper()