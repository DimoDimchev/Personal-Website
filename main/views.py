from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Project


class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectsView(ListView):
    model = Project
    template_name = 'projects.html'
