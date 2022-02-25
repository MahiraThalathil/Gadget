from tkinter import CASCADE
from django.db import models

# Create your models here.
class register(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=200,unique=True)
    phone=models.CharField(max_length=200,unique=True)
    email=models.EmailField(max_length=200,unique=True)
    password1=models.CharField(max_length=100,unique=True)
    password2=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.username

class login(models.Model):
    username=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=200,unique=True)
    

    def __str__(self):
        return self.username
