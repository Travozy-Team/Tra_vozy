from django.urls import path
from  . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
    path('tour-packages/', views.tour_packages, name='tour-packages'),
    path('hajj/', views.hajj, name='hajj'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),



    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('login-page/', views.login_page, name='login_page'),  # redirect to index?show=login
    path('register-page/', views.register_page, name='register_page'),  # redirect to index?show=register
]