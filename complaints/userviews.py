from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *




def user(request):
    return render(request, 'user.html')
    


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
        complainant_email = request.POST.get('name')
        complaint_dob = request.POST.get('name')
        complainant_address = request.POST.get('name')
        complainant_state_name = request.POST.get('name')
        complainant_state_id = request.POST.get('name')
        complainant_district_name = request.POST.get('name')
        complainant_district_id = request.POST.get('name')
        complainant_pin_code = request.POST.get('name')
        state_name = request.POST.get('name')
        state_id = request.POST.get('name')
        district_name = request.POST.get('name')
        district_id = request.POST.get('name')
        station_name = request.POST.get('name')
        station_id = request.POST.get('name')
        status_id = request.POST.get('name')
        crime_category = request.POST.get('name')
        other_crime_category = request.POST.get('name')
        subject = request.POST.get('name')
        detailed_description = request.POST.get('name')
        delay_reason = request.POST.get('name')
        datetime_of_occurence = request.POST.get('name')
        place_of_occurence = request.POST.get('name')
        evidence_image = request.POST.get('name')
        created_at = request.POST.get('name')
        updated_at = request.POST.get('name')



        
        crime_category = request.POST.get('crime_category')
        crime_category_object = crime_category_master.objects.get(crime_category_name=crime_category)
        crime_category_id = crime_category_object.crime_category_id
        print(crime_category,crime_category_id)
        return redirect('/user')
    
    

    else:
        return render(request, 'create_complaint.html',context)