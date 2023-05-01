from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from complaints.models import district_master,state_master,police_station_master
from django.http import HttpResponseRedirect
from accounts.models import *

def landing_page(request):
    return render(request,"landing_page.html")

from django.shortcuts import render, redirect
from accounts.models import *

def register(request):
    states = state_master.objects.all()
    district = district_master.objects.all()
    context = {
                'states': states,
                'district': district,
    }
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
        state = request.POST.get('complainant_state')
        district = request.POST.get('complainant_district')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')

        states = state_master.objects.get(state_name=state)
        print(states.state_name)

        districts = district_master.objects.get(district_name=district)
        print(districts.district_name)
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
            state=states,
            district=districts,
            address=address,
            pincode=pincode,
            state_id_no =states.state_id,
            district_id_no = districts.district_id
        )

        # Redirect to the login page
        return redirect(reverse('landing_page'))
    
    # Render the form for GET requests
    print(context)
    return render(request, 'register.html',context)


def user_login(request):
    if request.method == 'POST':
        context = {'Login_status': ''}

        # get the username and password from the POST request
        email1  = request.POST.get('email')
        password1  = request.POST.get('password')
        
        print(email1)
        print(password1)
        user = None
        try:
            user = CustomUser.objects.get(email=email1)
            print("user")
        except :
            try:
                user = police_incharge.objects.get(email=email1)
                print("psi")
            except :
                print("psi not exist")
                try:
                    user = police_officer.objects.get(email=email1)
                    print("police")
                except :
                    print("police not exist")
                    context.update({'Login_status':"Invalid credentials"})
                    print(context['Login_status'])
                    return render(request, 'login.html',context)

        # authenticate the user
        if user is not None:
            print("fetching")
            authenticate_user = authenticate(request, email=email1, password=password1)
            
            if authenticate_user is not None:
                print("fetched")
                print(user)
                if authenticate_user is not None:

                    if isinstance(authenticate_user, CustomUser):
                        login(request, user,backend='accounts.auth.CustomUserBackend')
                        context.update({'Login_status':""})
                        print(context['Login_status'])
                        return redirect('/user')
                    
                    elif isinstance(authenticate_user, police_incharge):
                        login(request, user,backend='accounts.auth.PoliceInchargeBackend')
                        context.update({'Login_status':""})
                        print(context['Login_status'])
                        return  redirect('/test') 
                    
                    elif isinstance(authenticate_user, police_officer):
                        login(request, user,backend='accounts.auth.PoliceBackend')
                        context.update({'Login_status':""})
                        print(context['Login_status'])
                        return  redirect('/police') 
                else:
                    context.update({'Login_status':"Invalid credentials"})
                    print(context['Login_status'])
                    return render(request, 'login.html',context)
            else:
                return  HttpResponse("user not found")

    else:
        # render the login page
        return render(request, 'login.html')
    


def user_logout(request):
    logout(request)
    return redirect('landing_page')

def index(request):
    return render(request, 'index.html')

def get_districts(request):
    state_name = request.GET.get('complaint_state') 
    state_object = state_master.objects.get(state_name=state_name)
    state_id = state_object.state_id
    districts_objects = district_master.objects.filter(state_id=state_id)
    districts = list(districts_objects.values('district_id', 'district_name'))
    return JsonResponse({'districts': districts})

def get_police_stations(request):
    district_name = request.GET.get('complaint_district') 
    district_object = district_master.objects.get(district_name=district_name)
    district_id = district_object.district_id
    police_station_objects = police_station_master.objects.filter(district_id=district_id)
    # print(police_station_objects)
    police_stations = list(police_station_objects.values('station_id', 'station_name'))
    # print(police_stations)
    return JsonResponse({'police_stations': police_stations})



def get_districts_register(request):
    state_name = request.GET.get('complainant_state') 
    state_object = state_master.objects.get(state_name=state_name)
    state_id = state_object.state_id
    districts_objects = district_master.objects.filter(state_id=state_id)
    districts = list(districts_objects.values('district_id', 'district_name'))
    return JsonResponse({'districts': districts})


def sidebar(request):
    return render(request, 'sidebar.html')

def administrator(request):
    return render(request, 'admin.html')



def test(request):
    return render(request, 'test.html')

def police(request):
    return render(request, 'police.html')


