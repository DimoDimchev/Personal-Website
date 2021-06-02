from django.db import models
from cloudinary import models as cloudinary_models


class Project(models.Model):
    name = models.CharField(max_length=100)
    github = models.CharField(max_length=300)
    website = models.CharField(max_length=300, blank=True)
    used_technologies = models.CharField(max_length=500)
    description = models.TextField()
    short_description = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
