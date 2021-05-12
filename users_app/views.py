from django.shortcuts import render, redirect          
from .models import *
# Create your views here.
def index(request):
     all_users = User.objects.all()
     context ={
          "all_users": all_users

     }
     return render (request,'index.html', context)

def add_user(request):
     if request.method == "POST":
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          email_address = request.POST['email_address']
          age = request.POST['age']
          User.objects.create(first_name=first_name,last_name=last_name, email_address=email_address, age=age)
     return redirect("/")
