from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ahkrweb.constant import USER_TYPE


# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(verbose_name = "User type", max_length = 50, choices = USER_TYPE, blank = False, null = False)
    profile_pic = models.ImageField(upload_to='images/', blank=True, null = True)

    def __str__(self):
        return self.user.username
