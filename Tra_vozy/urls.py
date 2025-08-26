from django.urls import path
from  . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
    path('tour-packages/', views.tour_packages, name='tour-packages'),
    path('hajj/', views.hajj, name='hajj'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]