from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']







class Booking(models.Model):
    PACKAGE_TYPES = [
        ('tour', 'Tour Package'),
        ('hajj', 'Hajj Package'),
    ]
    
    # Package information
    package_id = models.CharField(max_length=50)
    package_type = models.CharField(max_length=10, choices=PACKAGE_TYPES, default='tour')
    package_title = models.CharField(max_length=200)
    package_price = models.CharField(max_length=100)
    
    # Customer information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Booking details
    travel_date = models.DateField()
    number_of_travelers = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    
    # Metadata
    booking_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='pending')
    
    class Meta:
        ordering = ['-booking_date']
    
    def __str__(self):
        return f"{self.full_name} - {self.package_title}"


