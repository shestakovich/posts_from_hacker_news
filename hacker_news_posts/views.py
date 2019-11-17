from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView

from hacker_news_posts.forms import ParamsForm
from hacker_news_posts.models import Post
from hacker_news_posts.serializers import PostSerializer


class PostsListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ParamsForm(self.request.GET)

        if form.is_valid():
            order = form.cleaned_data.get('order')
            if order:
                queryset = queryset.order_by(order)

            offset = form.cleaned_data.get('offset') or 0
            limit = form.cleaned_data.get('limit') or 5
            return queryset[offset:offset+limit]

        else:
            raise ParseError(form.errors)
