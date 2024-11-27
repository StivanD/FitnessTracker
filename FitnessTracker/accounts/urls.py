from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserLoginView, UserRegisterView, EditProfileView, ProfileDetailsView, ChangePasswordView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', EditProfileView.as_view(), name='edit-profile'),
    path('details/', ProfileDetailsView.as_view(), name='profile-details'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
]