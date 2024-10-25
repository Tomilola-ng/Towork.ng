""" Seek Artisans Models """
# pylint: disable=no-member

from django.db import models
from django.utils import timezone
from django.urls import reverse

from users.models import Profile
from workers.models import Job


class Seek(models.Model):
    """ Seek Artisans """
    profile = models.ForeignKey(
        Profile, related_name='seeks', on_delete=models.CASCADE)
    budget = models.PositiveIntegerField(verbose_name='Your Budget in Naira')
    active = models.BooleanField(default=False)
    job = models.ForeignKey(
        Job, verbose_name='Select a service', on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=50)
    local_government = models.CharField(max_length=50)
    start_time = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return f'{self.profile.user} needs a {self.job} at {self.local_government}, {self.state}'

    def get_absolute_url(self):
        """ Get the absolute URL for the Seek Instance """
        return reverse('seek-detail', kwargs={'pk': self.id})

    class Meta:
        """ Meta """
        ordering = ['-start_time']
