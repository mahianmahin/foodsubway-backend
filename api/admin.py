from django.contrib import admin

from .models import *


@admin.register(User_info)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'district']
