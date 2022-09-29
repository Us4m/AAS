from ast import If
import email
from multiprocessing import context
from os import name
from django.shortcuts  import render, HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is variable"
    }
   
    return render(request,'home.html')
    # return HttpResponse("this is home")

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        contact =Contact( name= name, email= email, ph=ph, date=datetime.today() )
        contact.save()
        messages.success(request, 'Message sent sucessfully our team get in touch soon.')

    return render(request,'contactus.html')

def portfolio(request):
    return render(request,'portfolio.html')

def team(request):
    return render(request,'team.html')
    