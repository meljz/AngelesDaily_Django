from django.urls import path
from . import views

urlpatterns = [
    path ('news/', views.news_list, name='news_list'),
    path ('articles/<int:pk>/', views.Articles_detail, name='articles_detail'),

    path ('blog/', views.blog_post, name="blog_post"),
    path ('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
]