from django.shortcuts import render, redirect
from .models import Flight, HotelBooking, Meeting, BusinessPartner
from .forms import BusinessPartnerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def business_partner_schedule(request, business_partner_id):
    business_partner = BusinessPartner.objects.get(id=business_partner_id)
    flights = Flight.objects.filter(business_partner=business_partner)
    hotel_bookings = HotelBooking.objects.filter(business_partner=business_partner)
    meetings = Meeting.objects.filter(business_partner=business_partner)

    context = {
        'business_partner': business_partner,
        'flights': flights,
        'hotel_bookings': hotel_bookings,
        'meetings': meetings,
    }

    return render(request, 'resources/business_partner_schedule.html', context)

def home(request):
    business_partner = BusinessPartner.objects.get(name='Julius Benz')
    flights = Flight.objects.filter(business_partner=business_partner)
    hotel_bookings = HotelBooking.objects.filter(business_partner=business_partner)
    meetings = Meeting.objects.filter(business_partner=business_partner)

    context = {
        'business_partner': business_partner,
        'flights': flights,
        'hotel_bookings': hotel_bookings,
        'meetings': meetings,
    }
    
    return render(request, 'home.html', context)

def flight_list(request):
    return render(request, 'flight_list.html')

def add_business_partner(request):
    if request.method == 'POST':
        form = BusinessPartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BusinessPartnerForm()
    return render(request, 'add_business_partner.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})