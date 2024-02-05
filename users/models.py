from django.db import models
from django.contrib.auth.models import User
from .choices import localGovts, states, gender


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE)
    picture = models.ImageField(
        default = 'default.jpg', 
        upload_to='profile_pics')
    local_government = models.CharField(
        choices = localGovts, 
        default='Agege', 
        max_length=50, 
        verbose_name='Local Government you reside')
    state = models.CharField(
        choices=states , 
        default='Ogun',
        max_length=50, 
        verbose_name='State you reside?')
    gender = models.CharField(
        choices=gender,
        max_length=6, 
        default='Male')
    bio = models.TextField(
        verbose_name='Write a few things about yourself')
    phone = models.PositiveBigIntegerField(
        verbose_name='Phone Number',
        default=''
    )

    def __str__(self):
        return f'{self.user.username} Profile'