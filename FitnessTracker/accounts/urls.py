from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserLoginView, UserRegisterView, EditProfileView, ProfileDetailsView, CustomPasswordResetView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('details/<str:username>/', ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', EditProfileView.as_view(), name='edit-profile'),
    path('change-password/', CustomPasswordResetView.as_view(), name='reset-password'),
]