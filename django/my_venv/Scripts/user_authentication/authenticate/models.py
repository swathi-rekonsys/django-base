from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('Email Must Be Provide...')
        
        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        user.is_activate=True
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class User(AbstractUser):
    email=models.EmailField(max_length=100,primary_key=True)
    username=models.CharField(max_length=100)
   
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['password','username']



    objects=UserManager()
