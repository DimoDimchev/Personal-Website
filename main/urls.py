from django.urls import path

from main.views import IndexView, ProjectsView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('about/', AboutView.as_view(), name='about'),
]
