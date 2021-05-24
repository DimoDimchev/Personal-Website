from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='public/thumbnails')
    github = models.CharField(max_length=300)
    used_technologies = models.CharField(max_length=500)
    short_description = models.TextField()
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
