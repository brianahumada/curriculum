from django.urls import path
from .views import resume_view, index_view ,about_view

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('resume/', resume_view, name='resume'),
]
