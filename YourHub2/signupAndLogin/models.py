from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Items(models.Model):
    Item = models.CharField(max_length=100,null=True,blank=True)
    Itemuser = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Itemuser)
    
    
    
