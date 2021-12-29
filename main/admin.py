from django.contrib import admin

from main.models import Project, BlogPost, ProfileDescription

admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(ProfileDescription)