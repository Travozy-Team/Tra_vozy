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
    
    


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('bkash', 'bKash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket'),
        ('bank', 'Bank Transfer'),
    ]
    
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE, related_name='payment')
    card_name = models.CharField(max_length=100)
    package_id = models.CharField(max_length=50, default='default_value') 
    card_number = models.CharField(max_length=16)  
    exp_month = models.CharField(max_length=20)
    exp_year = models.CharField(max_length=4)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='card')
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    payment_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment for {self.booking.full_name} - {self.booking.package_title}"
    
    def save(self, *args, **kwargs):
        
        if not self.transaction_id:
            self.transaction_id = f"TXN{self.booking.id}{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'travozy_newslettersubscriber'  # ADD THIS LINE - matches your manually created table
        ordering = ['-subscribed_at']
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"     