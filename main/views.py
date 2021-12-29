from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View

from main.models import Project, BlogPost, ProfileDescription


class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectsView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    ordering = ['-date']


class ProjectDetailView(DetailView):
    template_name = 'project_details.html'
    model = Project


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    context_object_name = 'blog'
    ordering = ['-date']


class BlogDetailView(DetailView):
    template_name = 'blog_details.html'
    model = BlogPost


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_description'] = ProfileDescription.objects.first()
        return context
