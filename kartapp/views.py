from django.shortcuts import render
from product.models import *
# Create your views here.

def index(request):
    products = Product.objects.all().filter(is_available=True)
    context ={
        "products": products
    }
    return render(request,"index.html",context)

def signup_page(request):
    return render(request,"register.html")

def login_page(request):
    return render(request,"signin.html")

def store(request):
    return render(request,"store.html")