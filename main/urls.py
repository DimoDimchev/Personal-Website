from django.contrib.sitemaps.views import sitemap
from django.urls import path
from main.sitemaps import blog_dict, StaticViewSitemap
from django.contrib.sitemaps import GenericSitemap


from main.views import IndexView, ProjectsView, AboutView, ProjectDetailView, BlogView, BlogDetailView

sitemaps = {
    'blog': GenericSitemap(blog_dict, priority=0.5),
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project details'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog post details'),
    path('about/', AboutView.as_view(), name='about'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

