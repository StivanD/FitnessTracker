from django.contrib.auth import login, get_backends
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, CreateView, UpdateView

from FitnessTracker.accounts.forms import UserRegisterForm, UserLoginForm, UserProfileEditForm, CustomPasswordResetForm
from FitnessTracker.accounts.models import Profile, AppUser


# Create your views here.
class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = AppUser
    template_name = "profiles/profile-details.html"
    context_object_name = 'user'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(AppUser, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_own_profile'] = self.request.user == self.get_object()
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profiles/edit-profile.html"
    form_class = UserProfileEditForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_initial(self):
        initial = super().get_initial()
        initial['username'] = self.request.user.username
        initial['email'] = self.request.user.email
        initial['date_of_birth'] = self.request.user.date_of_birth
        return initial

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.save(commit=True)
        user = self.request.user

        user.save()

        return super().form_valid(form)


class CustomPasswordResetView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profiles/reset-password.html'
    form_class = CustomPasswordResetForm

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data['new_password1'])
        user.save()
        return super().form_valid(form)
