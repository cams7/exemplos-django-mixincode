# -*- coding: utf-8 -*-
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from aula12.models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    user = instance
    if not UserProfile.objects.filter(user=user):
        profile = UserProfile(user=user)
        profile.save()
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def my_callback(sender, **kwargs):
    print("My callback!")

