from django.contrib import admin

from .models import Booking

# admin.site.register(Booking)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=('firstname', 'lastname', 'title', 'phone_number', 'email', 'booked_date', 'booked_time', 'guests_number', 'customer_notes', 'is_vegetarian', 'is_vegan', 'is_subscribed')