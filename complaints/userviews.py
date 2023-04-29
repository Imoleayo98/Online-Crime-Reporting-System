from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='user_login')
def user(request):
    return render(request, 'user.html')
    
@login_required(login_url='user_login')
def create_complaint(request):
    crime_categories = crime_category_master.objects.all()
    states = state_master.objects.all()
    district = district_master.objects.all()
    police_stations =police_station_master.objects.all()
    context = {
                'crime_categories': crime_categories,
                'states': states,
                'districts': district,
                'police_stations':police_stations
    }
    if request.method == 'POST':
        complaint_name = request.POST.get('name')
        complainant_gender = request.POST.get('gender')
        complainant_contact_no = request.POST.get('contact_no')
        complainant_email = request.POST.get('email')
        complaint_dob = request.POST.get('dob')
        # 
        complainant_address = request.POST.get('')
        complainant_pin_code = request.POST.get('')
        state_name = request.POST.get('name')
        state_id = request.POST.get('name')
        district_name = request.POST.get('name')
        district_id = request.POST.get('name')
        # 
        complainant_state_name = request.POST.get('complaint_state')
        complainant_state_id = state_master.objects.get(state_name=complainant_state_name).state_id
        complainant_district_name = request.POST.get('complaint_district')
        complainant_district_id = district_master.objects.get(district_name=complainant_district_name).district_id
        station_name = request.POST.get('complaint_police_station')
        station_id = police_station_master.objects.get(station_name=station_name).station_id
        crime_category = request.POST.get('crime_category')
        other_crime_category = request.POST.get('other_crime_category')
        subject = request.POST.get('subject')
        detailed_description = request.POST.get('detailed_description')
        delay_reason = request.POST.get('delay_in_complaining')
        datetime_of_occurence = request.POST.get('date_time_of_occurence')
        place_of_occurence = request.POST.get('place_of_occurence')
        evidence_image = request.POST.get('evidence_image')
        # created_at = request.POST.get('name')
        # updated_at = request.POST.get('name')



        return redirect('/user')
    
    

    else:
        return render(request, 'create_complaint.html',context)