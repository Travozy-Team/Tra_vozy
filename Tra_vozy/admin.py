# admin.py
from django.contrib import admin
from .models import Booking



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'email', 'package_title', 'package_type', 
        'travel_date', 'number_of_travelers', 'booking_date', 'status'
    ]
    list_filter = ['package_type', 'status', 'booking_date', 'travel_date']
    search_fields = ['full_name', 'email', 'phone', 'package_title']
    readonly_fields = ['booking_date']
    list_per_page = 25
    
    fieldsets = (
        ('Package Information', {
            'fields': ('package_id', 'package_type', 'package_title', 'package_price')
        }),
        ('Customer Information', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Booking Details', {
            'fields': ('travel_date', 'number_of_travelers', 'special_requests')
        }),
        ('Status & Metadata', {
            'fields': ('status', 'booking_date')
        })
    )



