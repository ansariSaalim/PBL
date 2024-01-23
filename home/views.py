from django.shortcuts import render

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