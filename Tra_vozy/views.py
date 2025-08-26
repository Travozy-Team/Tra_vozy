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

