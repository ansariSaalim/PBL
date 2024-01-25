from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.core.serializers import serialize
import requests

from .models import vehicle
def map(request):
    queryset = vehicle.objects.all()

    vehicles_data = []
    for v in queryset:  # Change the loop variable name to 'v'
        try:
            current_location_parts = v.current_location.split(',')
            destination_parts = v.destination.split(',')

            if len(current_location_parts) != 2 or len(destination_parts) != 2:
                # Skip this record if the format is not as expected
                continue

            current_location = {
                'latitude': float(current_location_parts[0]),
                'longitude': float(current_location_parts[1]),
            }
            destination = {
                'latitude': float(destination_parts[0]),
                'longitude': float(destination_parts[1]),
            }
            vehicles_data.append({'current_location': current_location, 'destination': destination})
        except (ValueError, IndexError):
            # Handle the case where conversion to float or splitting fails
            # Log the error or take other appropriate actions
            pass

    context = {'vehicles_json': vehicles_data}
    return render(request, 'crm/map_result.html', context)





# Create your views here.
def home(request):
    return render(request,'crm/index.html')
def about(request):
    return render(request,'crm/about.html')
def personal_vehicle(request):
    if request.method == 'POST':
        current_location = request.POST.get('current')
        destination = request.POST.get('destination')
        mileage = request.POST.get('mileage')
        
        en = vehicle(
            current_location = current_location,
            destination = destination,
            mileage = mileage
        )
        en.save()
        # return redirect('/maps/')
        
    return render(request,'crm/personal.html')
def car(request):
    return render(request,'crm/personal.html')
def others(request):
    return render(request,'crm/others.html')
