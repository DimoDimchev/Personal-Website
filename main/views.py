from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Project, BlogPost


class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectsView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'project_details.html'
    model = Project


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'blog'


class BlogDetailView(DetailView):
    template_name = 'blog_details.html'
    model = BlogPost


class AboutView(TemplateView):
    template_name = 'about.html'
