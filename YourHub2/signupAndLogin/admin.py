from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Items
# Register your models here.

admin.site.register(Items)
