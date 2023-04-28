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
        name = request.POST.get('name')
        crime_category = request.POST.get('crime_category')
        crime_category_object = crime_category_master.objects.get(crime_category_name=crime_category)
        crime_category_id = crime_category_object.crime_category_id
        print(crime_category,crime_category_id)
        return redirect('/user')
    
    

    else:
        return render(request, 'create_complaint.html',context)