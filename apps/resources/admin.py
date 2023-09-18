from django.contrib import admin
from apps.resources.models import Flight, HotelBooking, Meeting, BusinessPartner
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'arrival_location', 'departure_location', 'arrival', 'departure')
    list_filter = ('arrival_location', 'departure_location')
    search_fields = ('flight_number', 'arrival_location', 'departure_location')

admin.site.register(BusinessPartner)
admin.site.register(Flight, FlightAdmin)
admin.site.register(HotelBooking)
admin.site.register(Meeting)