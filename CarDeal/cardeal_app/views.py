from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def cars(request):
    return render(request, 'cars.html')


def car_detail(request):
    return render(request, 'car_details.html')