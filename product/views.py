from django.shortcuts import render,get_object_or_404
from product.models import *
# Create your views here.

def store(request,categories_slug = None):
    cats = Category.objects.all()
    categories = None
    products = None
    if categories_slug != None:
        categories = get_object_or_404(Category,slug=categories_slug)
        products = Product.objects.all().filter(category=categories,is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context={
        "products":products,
        "count":product_count,"cats":cats
    }
    return render(request,"store/store.html",context)


def product_details(request,categories_slug,product_slug):
    single_product = Product.objects.get(category__slug=categories_slug,slug=product_slug)
    context = {
        "single_product":single_product
    }
    return render(request,"store/product-detail.html",context)
