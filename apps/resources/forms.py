from django import forms
from .models import BusinessPartner
from .models import Meeting

class BusinessPartnerForm(forms.ModelForm):
    class Meta:
        model = BusinessPartner
        fields = ['name']

class ProposeMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'start_time', 'end_time', 'location']