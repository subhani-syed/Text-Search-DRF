from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Paragraph,CustomUser

# Register your models here.

class UserAdmin(BaseUserAdmin):
    class UserChangeForm(forms.ModelForm):
        password = ReadOnlyPasswordHashField()

        class Meta:
            model = CustomUser
            fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser')

admin.site.register(Paragraph)
admin.site.register(CustomUser,UserAdmin)
