from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    next_page = '/'