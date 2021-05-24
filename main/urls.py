from django.urls import path

from main.views import IndexView, ProjectsView, AboutView, ProjectDetailView, BlogView, BlogDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project details'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog post details'),
    path('about/', AboutView.as_view(), name='about'),
]
