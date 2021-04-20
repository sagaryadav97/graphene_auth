
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from .managers import WWFUserManager
from phonenumber_field.modelfields import PhoneNumberField
import json
from django.contrib.auth.models import UserManager



class LoginUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=75, blank=True, null=True)
    email = models.EmailField(_('email address'), null=True, blank=True, default=None)
    phone = PhoneNumberField(unique=True)
    is_vendor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=75, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    # objects = WWFUserManager()
    objects = UserManager()

    def __str__(self):
        return str(self.phone)


# class OTP(models.Model):
#     user = models.ForeignKey(WWFUser, on_delete=models.CASCADE)
#     last_otp = models.CharField(max_length=6)
#     otp_expiry = models.DateTimeField()

#     def __str__(self):
#         return self.user
# 

# class OTP(models.Model):
#     user = models.ForeignKey(WWFUser, on_delete=models.CASCADE)
#     otp = models.CharField(max_length=6)

#     def __str__(self):
#         return self.user



