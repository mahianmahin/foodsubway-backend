from django.contrib.auth.models import User
from django.db import models


class User_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to="user_profile_pics")
