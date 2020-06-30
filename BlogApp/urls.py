"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'BlogApp'

urlpatterns = [

#homepage
     path('', views.index, name='index'),
     path('blog', views.blog, name='blog'),
     path('post', views.post, name='post'),
     path('search', views.search, name='search'),
     
     
]