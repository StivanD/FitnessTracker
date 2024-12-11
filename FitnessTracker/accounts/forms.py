from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import EmailInput, TextInput, PasswordInput, DateField, DateInput, ClearableFileInput, NumberInput, \
    Textarea

from FitnessTracker.accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': "Enter Password"
            }
        )

        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': "Confirm Password"
            }
        )

        self.fields['date_of_birth'].required = True

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
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = "__all__"


class UserLoginForm(AuthenticationForm):
    """
    Custom login form that allows logging in with either email or username.
    """
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username or email',
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control',
        })
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom placeholders and styles.
        """
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email_or_username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Use the custom backend
        self.user_cache = authenticate(self.request, username=email_or_username, password=password)
        if self.user_cache is None:
            raise forms.ValidationError("Please enter a correct username/email and password.")
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your username'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email'
            }
        )
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        ),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['height', 'weight', 'short_description', 'profile_picture']

        widgets = {
            'profile_picture': ClearableFileInput(),
            'height': NumberInput(
                attrs={
                    'placeholder': 'Enter your height in cm'
                }
            ),
            'weight': NumberInput(
                attrs={
                    'placeholder': 'Enter your weight in kg'
                }
            ),
            'short_description': Textarea(
                attrs={
                    'placeholder': 'Enter a short bio about you',
                    'rows': 3
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reorder fields here
        self.fields = {
            'username': self.fields['username'],
            'email': self.fields['email'],
            'date_of_birth': self.fields['date_of_birth'],
            'height': self.fields['height'],
            'weight': self.fields['weight'],
            'short_description': self.fields['short_description'],
            'profile_picture': self.fields['profile_picture'],
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 2:
            raise ValidationError("The username must contain at least 2 symbols!")

        user_model = get_user_model()
        if user_model.objects.filter(username=username).exclude(id=self.instance.user.id).exists():
            raise ValidationError("This username is already taken.")

        return username

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        date_of_birth = cleaned_data.get("date_of_birth")

        user = self.instance.user
        if username:
            user.username = username
        if email:
            user.email = email
        if date_of_birth:
            user.date_of_birth = date_of_birth

        user.clean()

        return cleaned_data


class CustomPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter new password'
            }
        ),
        label='New Password',
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm new password'
            }
        ),
        label='Confirm New Password',
    )
