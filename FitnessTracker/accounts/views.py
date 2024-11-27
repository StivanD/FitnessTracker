from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from FitnessTracker.accounts.forms import UserRegisterForm, UserLoginForm


# Create your views here.
class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    template_name = 'registration/logout-confirm.html'


class EditProfileView(TemplateView):
    template_name = "profiles/edit-profile.html"


class ProfileDetailsView(TemplateView):
    template_name = "profiles/profile-details.html"


class ChangePasswordView(TemplateView):
    template_name = "profiles/change-password.html"


class ProgressPage(TemplateView):
    template_name = "profiles/progress.html"
