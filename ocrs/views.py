from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from complaints.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime
from accounts.models import *
import pytz

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
                        return  redirect('/police_incharge_home',user) 
                    
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

@login_required(login_url='landing_page')
def police_incharge_home(request):
    return render(request, 'police_incharge.html')

@login_required(login_url='landing_page')
def manage_complaint(request,complaint_id):
    print(complaint_id)
    complaints = complaint_master.objects.get(complaint_id=complaint_id)
    context = {
        'complaints':complaints,
        'complaint_id': complaint_id,
    }
    return render(request, 'manage_complaint.html',context)

@login_required(login_url='landing_page')
def police_incharge_view_complaint(request):
    # print("view called")
    complaints = complaint_master.objects.filter(station_name=request.user.station_name).order_by('-complaint_id')
    context = {'complaints':complaints}
    return render(request, 'police_incharge_view_complaint.html',context)


def register_fir_csr(request):
    if request.method == 'POST':
        complaint_type = request.POST.get('complaint_type')        
        complaint_id = request.POST.get('complaint_id')
        print(f"complaint_id: {complaint_type}")   
        complainant_name = request.POST.get('name')
        complainant_gender = request.POST.get('gender')
        complainant_contact_no = request.POST.get('contact_no')
        complainant_email = request.POST.get('email')
        complainant_dob = complaint_master.objects.get(complaint_id=complaint_id).complainant_dob
        complainant_address = request.POST.get('address')
        get_complainant_state_name = request.POST.get('complainant_state_name')
        complainant_state_name = state_master.objects.get(state_name=get_complainant_state_name)
        complainant_state_id = state_master.objects.get(state_name=get_complainant_state_name).state_id
        get_complainant_district_name = request.POST.get('complainant_district_name')
        complainant_district_name = district_master.objects.get(district_name=get_complainant_district_name)
        complainant_district_id = district_master.objects.get(district_name=get_complainant_district_name).district_id
        complainant_pin_code = request.POST.get('pincode')
        get_state_name = request.POST.get('state_name')
        state_name = state_master.objects.get(state_name=get_state_name)
        state_id = state_master.objects.get(state_name=get_state_name).state_id
        get_district_name = request.POST.get('district_name')
        district_name = district_master.objects.get(district_name=get_district_name)
        district_id = district_master.objects.get(district_name=get_district_name).district_id
        get_station_name = request.POST.get('station_name')
        station_name = police_station_master.objects.get(station_name=get_station_name)
        station_id = police_station_master.objects.get(station_name=get_station_name).station_id
        crime_category = crime_category_master.objects.get(crime_category_name=request.POST.get('crime_category'))
        other_crime_category = request.POST.get('other_crime_category')
        subject = request.POST.get('subject')
        detailed_description = request.POST.get('detailed_description')
        delay_reason = request.POST.get('delay_in_complaining')

        datetime_of_occurence = complaint_master.objects.get(complaint_id=complaint_id).datetime_of_occurence


        place_of_occurence = request.POST.get('place_of_occurence')
        evidence_image = complaint_master.objects.get(complaint_id=complaint_id).evidence_image
        info_by_station_incharge = request.POST.get('info_by_incharge')
        if(complaint_type == 'fir'):
            fir_no = request.POST.get('fir_no')
            act_and_sections = request.POST.get('act_and_sections')
            gd_number = request.POST.get('gd_number')
            type_of_information = request.POST.get('type_of_information')
            nearest_identifiable_place = request.POST.get('nearby_place')
            direction_and_distance_from_ps = request.POST.get('dist_from_ps')
            complaintant_religion = request.POST.get('complainant_religion')
            complaintant_caste = request.POST.get('complainant_caste')
            sus_acu_details = request.POST.get('sus_acu_details')
            properties_involved = request.POST.get('property_involved')
            property_value = request.POST.get('property_value')

            fir = fir_master.objects.create(
            fir_no = fir_no,
            complainant_name = complainant_name,
            complainant_gender = complainant_gender,
            complainant_contact_no = complainant_contact_no,
            complainant_email = complainant_email,
            complainant_dob = complainant_dob,
            complainant_address = complainant_address,
            complainant_state_name = complainant_state_name,
            complainant_state_id = complainant_state_id,
            complainant_district_name = complainant_district_name,
            complainant_district_id = complainant_district_id,
            complainant_pin_code = complainant_pin_code,
            state_name = state_name,
            state_id = state_id,
            district_name = district_name,
            district_id = district_id,
            station_name = station_name,
            station_id = station_id,
            status_id = "FIR is Filed",
            crime_category = crime_category,
            other_crime_category = other_crime_category,
            subject = subject,
            fir_detailed_description = detailed_description,
            delay_reason = delay_reason,
            datetime_of_occurence = datetime_of_occurence,
            place_of_occurence = place_of_occurence,
            evidence_image = evidence_image,
            info_by_station_incharge = info_by_station_incharge,
            gd_number = gd_number,
            act_and_sections = act_and_sections,
            type_of_information = type_of_information,
            nearest_identifiable_place = nearest_identifiable_place,
            direction_and_distance_from_ps = direction_and_distance_from_ps,
            complaintant_religion = complaintant_religion,
            complaintant_caste = complaintant_caste,
            sus_acu_details = sus_acu_details,
            properties_involved = properties_involved,
            property_value = property_value,
            created_at = timezone.now(),
            updated_at = timezone.now()
            )
            complaint = complaint_master.objects.get(complaint_id=complaint_id)
            complaint.status = "FIR is Filed"
            complaint.save()
            return redirect('police_incharge_view_complaint')



        elif(complaint_type == 'csr'):
            csr_no = request.POST.get('csr_no')
            print(csr_no)
            csr = csr_master.objects.create(
                csr_no=csr_no,
                complainant_name = complainant_name,
                complainant_gender = complainant_gender,
                complainant_contact_no = complainant_contact_no,
                complainant_email = complainant_email,
                complainant_dob = complainant_dob,
                complainant_address = complainant_address,
                complainant_state_name = complainant_state_name,
                complainant_state_id = complainant_state_id,
                complainant_district_name = complainant_district_name,
                complainant_district_id = complainant_district_id,
                complainant_pin_code = complainant_pin_code,
                state_name = state_name,
                state_id = state_id,
                district_name = district_name,
                district_id = district_id,
                station_name = station_name,
                station_id = station_id,
                status_id = "CSR is Filed",
                crime_category = crime_category,
                other_crime_category = other_crime_category,
                subject = subject,
                ncr_detailed_description = detailed_description,
                delay_reason = delay_reason,
                datetime_of_occurence = datetime_of_occurence,
                place_of_occurence = place_of_occurence,
                evidence_image = evidence_image,
                info_by_station_incharge = info_by_station_incharge,
                created_at = timezone.now(),
                updated_at = timezone.now()
            )
            print(csr)
            complaint = complaint_master.objects.get(complaint_id=complaint_id)
            complaint.status = "CSR is Filed"
            complaint.save()
            return redirect('police_incharge_view_complaint')
        
        else:
            complaint = complaint_master.objects.get(complaint_id=complaint_id)
            complaint.status = 'Rejected'
            complaint.save()
            return redirect('police_incharge_view_complaint')
    else:
        return redirect('police_incharge_view_complaint')