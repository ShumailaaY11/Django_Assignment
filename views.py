# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Welcome to home page...")

# def aboutUs(request):
#     return HttpResponse("About Us...")

# def contact(request):
#     return HttpResponse("Contact Us...")

# def register(request):
#     return HttpResponse("Register Page...")

# def login(request):
#     return HttpResponse("Login Page...")


#Create 5 urls and views for home, about, services, privacy, blogs using template engine.

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def privacy(request):
    return render(request, 'privacy.html')

def blogs(request):
    return render(request, 'blogs.html')

