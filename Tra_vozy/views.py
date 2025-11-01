from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Booking
from .forms import BookingForm
from .models import Contact
from .models import  Payment 


def register_view(request):
    """
    Handle user registration
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation
        if not all([username, email, password1, password2]):
            messages.error(request, 'All fields are required.')
            # Redirect to index with register form showing
            return HttpResponseRedirect(reverse('index') + '?show=register')
            
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return HttpResponseRedirect(reverse('index') + '?show=register')
            
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return HttpResponseRedirect(reverse('index') + '?show=register')
            
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return HttpResponseRedirect(reverse('index') + '?show=register')
            
        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            user.save()
            
            messages.success(request, 'Registration successful! Please login.')
            
            return HttpResponseRedirect(reverse('index') + '?show=login')
            
        except Exception as e:
            messages.error(request, 'Registration failed. Please try again.')
            return HttpResponseRedirect(reverse('index') + '?show=register')
    
  
    return HttpResponseRedirect(reverse('index') + '?show=register')


def login_view(request):
    """
    Handle user login
    """
    if request.method == 'POST':
        username = request.POST.get('username')  
        email = request.POST.get('email')  
        password = request.POST.get('password')
        
         
        login_field = username or email
        
        if not all([login_field, password]):
            messages.error(request, 'Email and password are required.')
            return HttpResponseRedirect(reverse('index') + '?show=login')
        
        # Try to authenticate with username first
        user = authenticate(request, username=login_field, password=password)
        
        # If failed and input looks like email, try to find user by email
        if user is None and '@' in login_field:
            try:
                user_obj = User.objects.get(email=login_field)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect back to index.html after successful login
        else:
            messages.error(request, 'Invalid credentials.')
            return HttpResponseRedirect(reverse('index') + '?show=login')
    
    return HttpResponseRedirect(reverse('index') + '?show=login')


def index(request):
    """
    Home page view - handles both forms
    """
    # Check if we need to show registration or login form
    show = request.GET.get('show', '')
    context = {
        'show_register': show == 'register',
        'show_login': show == 'login'
    }
    
    return render(request, 'Tra_vozy/index.html', context)


def login_page(request):
    """
    Redirect to index with login form
    """
    return HttpResponseRedirect(reverse('index') + '?show=login')


def register_page(request):
    """
    Redirect to index with register form  
    """
    return HttpResponseRedirect(reverse('index') + '?show=register')






def index(request):
    return render(request, 'Tra_vozy/index.html')

def about(request):
    return render(request,'Tra_vozy/about.html')


def tour_packages(request):
    return render(request, 'Tra_vozy/tour-packages.html')

def hajj(request):
    return render(request, 'Tra_vozy/hajj.html')

def services(request):
    return render(request, 'Tra_vozy/services.html')

def contact(request):
    return render(request, 'Tra_vozy/contact.html')


def package_details(request):
    return render(request, 'Tra_vozy/stpack.html')

def hajj_package_details(request): 
    return render(request, 'Tra_vozy/shajjpack.html')

def booking_form(request):
    return render(request, 'Tra_vozy/form.html')


def booking_page(request):
    """Display the booking form page"""
    form = BookingForm()
    return render(request, 'your_booking_template.html', {'form': form})

def payment_page(request, booking_id=None):
    """Display the payment page"""
    context = {}
    if booking_id:
        try:
            booking = Booking.objects.get(id=booking_id)
            context['booking'] = booking
        except Booking.DoesNotExist:
            pass
    return render(request, 'Tra_vozy/payment.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def submit_booking(request):
    """Handle booking form submission via AJAX"""
    try:
        # Get JSON data from request
        data = json.loads(request.body)
        
        # Create new booking instance
        booking = Booking(
            package_id=data.get('packageId'),
            package_type=data.get('packageType', 'tour'),
            package_title=data.get('packageTitle'),
            package_price=data.get('packagePrice'),
            full_name=data.get('fullName'),
            email=data.get('email').lower(),
            phone=data.get('phone'),
            travel_date=data.get('travelDate'),
            number_of_travelers=int(data.get('travelers', 1)),
            special_requests=data.get('specialRequests', '')
        )
        
        # Save to database
        booking.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Booking submitted successfully!',
            'booking_id': booking.id,
            'redirect_url': f'/payment/{booking.id}/'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error submitting booking: {str(e)}'
        })

def booking_list(request):
    """View all bookings (for admin)"""
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validate that all fields are provided
        if name and email and subject and message:
            # Create and save the contact entry
            contact_entry = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contact_entry.save()
            
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'Tra_vozy/contact.html')



@require_http_methods(["POST"])
def process_payment(request):
    """Handle payment form submission"""
    try:
        booking_id = request.POST.get('booking_id')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        cvv = request.POST.get('cvv')
        
        # Validate required fields
        if not all([booking_id, card_name, card_number, exp_month, exp_year, cvv]):
            messages.error(request, 'All payment fields are required.')
            return redirect('payment', booking_id=booking_id)
        
        # Get booking
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            messages.error(request, 'Booking not found.')
            return redirect('index')
        
        # payment record with package_id from booking
        payment_obj = Payment(
            booking=booking,
            package_id=booking.package_id, 
            card_name=card_name,
            card_number=card_number[-4:], 
            exp_month=exp_month,
            exp_year=exp_year,
            payment_status='completed',
            payment_method='card'
        )
        payment_obj.save()
        
        # booking status
        booking.status = 'confirmed'
        booking.save()
        
        return redirect('payment_success', booking_id=booking.id)
        
    except Exception as e:
        messages.error(request, f'❌ Payment processing failed: {str(e)}')
        if booking_id:
            return redirect('payment', booking_id=booking_id)
        return redirect('index')





