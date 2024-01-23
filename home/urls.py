from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name=''),
    path('about/',views.about,name='about'),
    path('personal/',views.personal_vehicle,name='personal_vehicle'),
    path('personal/cars/',views.car,name='car'),
    path('others/',views.others,name='others'),
]