from datetime import date
import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    ph = models.CharField(max_length=120)
    
    date = models.DateField()

    def __str__(self) :
        return self.name