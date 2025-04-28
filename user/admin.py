from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.forms import TextInput, Textarea
from django import forms

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields':('is_staff', 'is_active', 'is_superuser', 'groups' ,'user_permissions')}),
    )
  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
