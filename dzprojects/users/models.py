from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from PIL import Image
# Create your models here.


class Prof(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    nickname = models.CharField(
        max_length=255, null=True)
    work = models.CharField(max_length=255, blank=True, default="studiant")
    phone = models.CharField(max_length=12, blank=True, null=True)
    linkedin_link = models.URLField(max_length=255, blank=True)
    instagram_link = models.URLField(max_length=255, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    youtube_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    prof_views = models.IntegerField(default=0)
    image = models.ImageField(
        null=True, blank=True, upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return str(self.nickname)
