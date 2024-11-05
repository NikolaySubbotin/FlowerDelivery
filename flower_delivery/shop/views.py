# shop/views.py
from django.shortcuts import render
from .models import Product



def home(request):
    return render(request, 'home.html')


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})
