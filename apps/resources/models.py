from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase

# Create your models here.

class Tag(CreatedModifiedDateTimeBase):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)
    
    #class Meta:
    #   verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.cat
    
class BusinessPartner(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.name
        
class Flight(models.Model):
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    arrival_location = models.CharField(max_length=100)
    departure_location = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return self.flight_number
    
class HotelBooking(models.Model):
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.hotel_name

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
