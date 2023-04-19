from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def landing_page(request):
    return render(request,"landing_page.html")

from django.shortcuts import render, redirect
from accounts.models import *

def register(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        Phone_Number = request.POST.get('Phone_Number')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        password = request.POST.get('password')
        gender = request.POST.get('Yourgender')
        aadhaarno = request.POST.get('aadhaarno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')

        # Create the user object
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            Phone_Number=Phone_Number,
            first_name=first_name,
            last_name=last_name,
            password=password,
            gender=gender,
            aadhaarno=aadhaarno,
            country=country,
            state=state,
            city=city,
            address=address,
            pincode=pincode
        )

        # Redirect to the login page
        return render(request, 'login.html',)
    
    # Render the form for GET requests
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        # get the username and password from the POST request
        email  = request.POST.get('email')
        password  = request.POST.get('password')
        
        print(email)
        print(password)

        # authenticate the user
        if '@' in email:
            user = authenticate(request, email=email, password=password)
        else:
            user = authenticate(request, username=email, password=password)
        context = {'Login_status': ''}
        print(user)
        if user is not None:
            # the username and password are correct
            # login(request, user)
            context.update({'Login_status':""})
            print(context['Login_status'])
            return redirect('/index')
        else:
            # the username and/or password are incorrect
            # error_message = 'Invalid username or password'
            # return HttpResponse("Login Failed")
            context.update({'Login_status':"Invalid credentials"})
            print(context['Login_status'])
            return render(request, 'login.html',context)

    else:
        # render the login page
        return render(request, 'login.html')
    

def index(request):
    return render(request, 'index.html')