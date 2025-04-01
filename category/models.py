from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    category_image = models.ImageField(upload_to='photos/categories')
    description = models.TextField(blank=True)


    class meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def get_url(self):
        return reverse('product_by_slug',args=[self.slug])

    def __str__(self):
           return self.category_name
