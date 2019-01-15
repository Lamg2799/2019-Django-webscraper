from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from .models import Items
class CustomUCreationForm(UserCreationForm):
    email= forms.EmailField(label="Email",required=True)
    class Meta:
        model = User
        fields=["username","email","password1","password2"]
    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        #commit=false means dont save it to database but create object
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
        
    
