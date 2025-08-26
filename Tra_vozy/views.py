from django.shortcuts import render, redirect



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

