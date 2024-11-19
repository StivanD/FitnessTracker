from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit/', views.EditProfileView.as_view(), name='edit-profile'),
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('change-password', views.ChangePasswordView.as_view(), name='change-password')
]