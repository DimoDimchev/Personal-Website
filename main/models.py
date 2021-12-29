from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    github = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    website = models.CharField(max_length=300, blank=True)
    used_technologies = models.CharField(max_length=500)
    description = models.TextField()
    short_description = models.CharField(max_length=180)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project details', kwargs={'pk': self.pk})


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog post details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class ProfileDescription(models.Model):
    introduction = models.TextField()
    personal_skills = ArrayField(models.CharField(max_length=100), default=list)
