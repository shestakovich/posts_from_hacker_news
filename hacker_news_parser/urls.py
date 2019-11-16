from django.contrib import admin
from django.urls import path

from hacker_news_posts.views import PostsListView

urlpatterns = [
    path('posts/', PostsListView.as_view()),
]
