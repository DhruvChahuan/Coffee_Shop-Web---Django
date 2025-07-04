from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
    path("manu/", views.manu, name='Manu Page'),
    path("about/", views.about, name='About Page'),
    path("contact/", views.contact, name='contact Page'),
    path("ordernow/", views.ordernow, name='order now Page'),
]

