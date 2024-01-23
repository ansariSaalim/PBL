from django.shortcuts import render
from django.http import JsonResponse
import requests

def calculate_distance_cost(request):
    if request.method == 'POST':
        start_location = request.POST.get('start_location')
        end_destination = request.POST.get('end_destination')
        mileage = float(request.POST.get('mileage'))

        # Validate input data
        if not start_location or not end_destination or not mileage:
            return JsonResponse({'error': 'Please provide valid input data'})

        # Use Bing Maps Distance Matrix API to calculate distance
        bing_maps_api_key = 'AsQxFl6g4F3LyOFAaZjIj1Y_L0oTY879ZgmCfeDuQGT0rv-j3K_OOgCKN5kup1Dw'  # Replace with your actual Bing Maps API key
        endpoint = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix'
        params = {
            'origins': f'{start_location}',  # Assuming locations are in the USA
            'destinations': f'{end_destination}, ',
            'travelMode': 'driving',
            'key': bing_maps_api_key,
        }

        response = requests.get(endpoint, params=params)
        data = response.json()

        if response.status_code == 200 and 'resourceSets' in data and data['resourceSets']:
            # Extract distance in kilometers from the API response
            distance_in_kilometers = data['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']

            # Calculate cost based on mileage
            cost = mileage * distance_in_kilometers

            # Pass the calculated values to the template
            return render(request, 'crm/map_result.html', {
                'start_location': start_location,
                'end_destination': end_destination,
                'distance': distance_in_kilometers,
                'cost': cost
            })

        return JsonResponse({'error': 'Error calculating distance. Please try again.'})

    # If the request method is not POST, return an error response
    return JsonResponse({'error': 'Invalid request method'})

# Create your views here.
def home(request):
    return render(request,'crm/index.html')
def about(request):
    return render(request,'crm/about.html')
def personal_vehicle(request):
    return render(request,'crm/personal.html')
def car(request):
    return render(request,'crm/personal.html')
def others(request):
    return render(request,'crm/others.html')