from rest_framework.serializers import ModelSerializer

from hacker_news_posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'url',
            'created',
        )
