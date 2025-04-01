from django.urls import path
from product.views import *

urlpatterns = [

path('', store,name='store'),
path('<slug:categories_slug>/', store,name='product_by_slug'),
path('<slug:categories_slug>/<slug:product_slug>/', product_details,name='product_details'),
]
