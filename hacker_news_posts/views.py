from django.shortcuts import render
from rest_framework.generics import ListAPIView

from hacker_news_posts.models import Post
from hacker_news_posts.serializers import PostSerializer


class PostsListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.GET
        order = params.get('order')
        if order:
            queryset = queryset.order_by(order)
        offset = int(params.get('offset', 0))
        limit = int(params.get('limit', 5))
        return queryset[offset:offset+limit]
