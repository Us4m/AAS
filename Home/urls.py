from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
  path("", views.index, name='Home'),
  path("about", views.about, name='about'),
  path("contact", views.contact, name='contact'),
  path("services", views.services, name='services'),
  path("portfolio", views.portfolio, name='portfolio'),
  path("team", views.team, name='team'),
  

  
]
