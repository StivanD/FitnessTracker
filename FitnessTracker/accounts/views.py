from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LoginView(TemplateView):
    template_name = 'registration/login.html'


class RegisterView(TemplateView):
    template_name = 'registration/register.html'


class EditProfileView(TemplateView):
    template_name = "profiles/edit-profile.html"


class ProfileDetailsView(TemplateView):
    template_name = "profiles/profile-details.html"


class ChangePasswordView(TemplateView):
    template_name = "profiles/change-password.html"