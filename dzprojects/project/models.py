from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    author = models.CharField(max_length=256)
    author_id = models.CharField(max_length=256)
    author_avatar = models.CharField(max_length=256)
    website_link = models.CharField(null=True, blank=True, max_length=500)
    repository_link = models.CharField(null=True, blank=True, max_length=500)
    post_date = models.DateField(auto_now_add=True)
    project_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project')
