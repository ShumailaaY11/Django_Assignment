from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to home page...")

def aboutUs(request):
    return HttpResponse("About Us...")

def contact(request):
    return HttpResponse("Contact Us...")

def register(request):
    return HttpResponse("Register Page...")

def login(request):
    return HttpResponse("Login Page...")