from django.urls import path
from  . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
    path('tour-packages/', views.tour_packages, name='tour-packages'),
    path('hajj/', views.hajj, name='hajj'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('package-details/', views.package_details, name='package-details'),
    path('hajj-package-details/', views.hajj_package_details, name='hajj-package-details'),
path('booking_form/', views.booking_form, name='booking_form'),
    
    


    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('login-page/', views.login_page, name='login_page'),  # redirect to index?show=login
    path('register-page/', views.register_page, name='register_page'),  # redirect to index?show=register

    path('booking/', views.booking_page, name='booking'),
    path('submit-booking/', views.submit_booking, name='submit_booking'),
    path('admin/bookings/', views.booking_list, name='booking_list'),


    path('payment/<int:booking_id>/', views.payment_page, name='payment'),
    path('payment/', views.payment_page, name='payment'), 
    path('process-payment/', views.process_payment, name='process_payment'),  
    path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),
  
]