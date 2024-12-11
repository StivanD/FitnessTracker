from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import PermissionDenied

from .models import AppUser, Profile


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and obj.is_superuser:
            raise PermissionDenied("You cannot assign superuser status.")

        if not change:
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['groups'].queryset = form.base_fields['groups'].queryset.exclude(name='Superusers')
        return form

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['is_superuser', 'groups', 'user_permissions']
        return super().get_readonly_fields(request, obj)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'short_description')
    search_fields = ('user__email', 'user__username', 'short_description')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.exclude(user__is_superuser=True)
        return qs
