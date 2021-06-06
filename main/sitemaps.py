from django.contrib import sitemaps
from django.urls import reverse

from main.models import BlogPost, Project

blog_dict = {
    'queryset': BlogPost.objects.all(),
    'date_field': 'date',
}

project_dict = {
    'queryset': Project.objects.all(),
}


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'projects', 'blog']

    def location(self, item):
        return reverse(item)
