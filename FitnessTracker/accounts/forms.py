from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import EmailInput, TextInput, PasswordInput


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

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
