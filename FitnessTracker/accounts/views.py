from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LoginView(TemplateView):
    template_name = 'registration/login.html'


class RegisterView(TemplateView):
    template_name = 'registration/register.html'


class ProfileDetailsView(TemplateView):
    template_name = "profile-details.html"
