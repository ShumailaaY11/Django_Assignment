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

# from django.shortcuts import render


# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

# def services(request):
#     return render(request, 'services.html')

# def privacy(request):
#     return render(request, 'privacy.html')

# def blogs(request):
#     return render(request, 'blogs.html')




from django.shortcuts import render

students_data = [
    {'name': 'Ali', 'age': 20, 'roll_no': 1},
    {'name': 'Raza', 'age': 22, 'roll_no': 2},
    {'name': 'Haider', 'age': 25, 'roll_no': 3},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def students(request):
    return render(request, 'students.html', {'students': students_data})