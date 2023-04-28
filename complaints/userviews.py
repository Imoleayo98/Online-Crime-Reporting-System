from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *




def user(request):
    return render(request, 'user.html')
    


def create_complaint(request):
    crime_categories = crime_category_master.objects.all().values_list('crime_category_name', flat=True)
    context = {
                'crime_categories': crime_categories,

    }
    if request.method == 'POST':
        pass
    
    

    else:
        return render(request, 'create_complaint.html',context)
