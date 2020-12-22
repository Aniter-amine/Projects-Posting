from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Prof
import os


@receiver(post_save, sender=User)
def create_proimage(sender, instance, created, **kwargs):
    if created:
        Prof.objects.create(user=instance)
        print('Proimage Created')


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.prof.save()
        print('Profile Updated')
