from django.shortcuts import render,redirect
from django.contrib import messages
from .models import test1
from datetime import datetime

# Create your views here.

def home(request):
    if request.method == 'POST':
        x= test1()
        x.name= request.POST.get('name')
        x.username= request.POST.get('fname')
        x.password= request.POST.get('Password')
        x.dob= request.POST.get('DOB')
        x.save()
        print('added to database')
        # en = signupPage(name,fullname,password,DOB)
        # en.save()
        return render(request,'login.html')
    
    return render(request,'login.html')

# Login Function
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         dob = request.POST.get('dob')
#         password = request.POST.get('password')

#         try:
#             user = test1.objects.get(username=username,email=email,dob=dob,password=password)
#             # check the 4 fields for exact match in the database
#             if user is not None:
#                 print("User Successfully Detected") # Authentication confirmation
#                 context = {} # the data to pass to the webpage
#                 return render(request,loginone.html,context)
#             else:
#                 messages.info(request,'Wrong Details')
#                 return redirect('home')
#         except Exception as e:
#             messages.info(request,"Invalid Data")