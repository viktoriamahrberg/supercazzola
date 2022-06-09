from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
   
]