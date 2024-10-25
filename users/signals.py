""" Users Signals """
# pylint: disable=unused-argument

from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from users.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Create a profile for new users """
    if created:
        Profile.objects.create(user=instance)
