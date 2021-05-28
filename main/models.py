from django.db import models
from cloudinary import models as cloudinary_models


class Project(models.Model):
    name = models.CharField(max_length=100)
    image = cloudinary_models.CloudinaryField('image')
    github = models.CharField(max_length=300)
    website = models.CharField(max_length=300, blank=True)
    used_technologies = models.CharField(max_length=500)
    short_description = models.TextField(max_length=179)
    description = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
