# path('string to add to url to get to page',view to display, name of page)
from . import views
from django.urls import path

urlpatterns = [
    path('',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('newitem/',views.newitem,name='newitem'),
    path('currentprices/',views.currentprices,name='currentprices'),
    ]
