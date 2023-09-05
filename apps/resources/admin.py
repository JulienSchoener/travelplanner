from django.contrib import admin
from apps.resources.models import Flight, HotelBooking, Meeting, BusinessPartner

admin.site.register(BusinessPartner)
admin.site.register(Flight)
admin.site.register(HotelBooking)
admin.site.register(Meeting)