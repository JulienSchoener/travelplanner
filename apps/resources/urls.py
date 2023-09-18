from django.urls import path
from django.contrib import admin
from . import views
from .views import add_business_partner

urlpatterns = [
    path('', views.home, name='home'),
    path('flights/', views.flight_list, name='flight_list'), 
    path('business_partner/<int:business_partner_id>/schedule/', views.business_partner_schedule, name='business_partner_schedule'),
    path('add_business_partner/', add_business_partner, name='add_business_partner'),
]
