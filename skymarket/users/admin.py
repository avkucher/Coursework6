from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from django import forms
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

admin.site.register(User)


# class ContactForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'phone': PhoneNumberPrefixWidget(initial='RU'),
#         }
#
# @admin.register(User)
# class ContactAdmin(admin.ModelAdmin):
#     form = ContactForm
