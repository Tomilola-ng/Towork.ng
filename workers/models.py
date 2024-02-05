from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Job(models.Model):
    job = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.job}'

class Worker(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job,verbose_name='', on_delete=models.SET_NULL, null = True)
    account_number = models.IntegerField(null=True, default=1234567890)
    account_name = models.CharField(max_length=100, default='')
    bank = models.CharField(max_length=50, default='', help_text='Must be a Nigerian Bank')

    def __str__(self):
        return f'Worker { self.profile.user }'