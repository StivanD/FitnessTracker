from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, SetPasswordForm
from django.forms import EmailInput, TextInput, PasswordInput, DateField, DateInput

from FitnessTracker.accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'form-control',  # Add your custom class here
            'placeholder': 'MM/DD/YYYY',
        }),
        required=True,
        label='Date of Birth'
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']

        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Enter your username',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Enter your email',
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Enter your first name',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Enter your last name',
                }
            ),
            # 'date_of_birth': DateField(
            #     widget=forms.DateInput(attrs={
            #         'type': 'date',
            #         'placeholder': 'MM/DD/YYYY'
            #     }),
            #     required=True,
            #     label='Date of Birth'
            # ),
            'password1': PasswordInput(
                attrs={
                    'placeholder': 'Enter your password',
                }
            ),
            'password2': PasswordInput(
                attrs={
                    'placeholder': 'Confirm your password',
                }
            )
        }


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = "__all__"


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username or email',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
        })


class UserProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    class Meta:
        model = Profile
        fields = ['profile_picture', 'height', 'weight', 'short_description']


class CustomPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}),
        label='New Password',
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}),
        label='Confirm New Password',
    )