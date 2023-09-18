from django import forms
from .models import BusinessPartner

class BusinessPartnerForm(forms.ModelForm):
    class Meta:
        model = BusinessPartner
        fields = ['name']
