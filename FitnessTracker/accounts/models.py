from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models

from FitnessTracker.accounts.managers import AppUserManager


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(2, "The username must contain at least 2 symbols!")
        ]
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2, "The first name must contain at least 2 symbols!")
        ]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2, "The last name must contain at least 2 symbols!")
        ]
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


class Profile(models.Model):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True,
        default="default_images/default-profile-image.png"
    )

    height = models.FloatField(
        validators=[
            MinValueValidator(1, "The height must be a positive number!")
        ]
    )

    weight = models.FloatField(
        validators=[
            MinValueValidator(1, "The weight must be a positive number!")
        ]
    )

    short_description = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

