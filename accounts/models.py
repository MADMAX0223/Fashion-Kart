import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,user_name,email,password=None):
        if not email:
            raise ValueError('user must have email')
        if not user_name:
            raise ValueError('user must have user_name')
        user = self.model(
            email=self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,first_name,last_name,user_name,email,password):
        user= self.create_user(
        email = self.normalize_email(email),
        user_name = user_name,
        first_name = first_name,
        last_name = last_name,
        password = password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class Account(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    object = MyAccountManager()

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True



