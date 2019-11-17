import json

from django.test import TestCase, client
from rest_framework import status

from hacker_news_posts.models import Post
from hacker_news_posts.serializers import PostSerializer


class TestRequests(TestCase):
    def setUp(self):
        Post.objects.create(title='asd', url='http://asdf.ru')
        Post.objects.create(title='asd2', url='http://asdf.ru2')
        Post.objects.create(title='asd3', url='http://asdf.ru3')

    def test_valid_request(self):
        response = self.client.get('/posts/', {'order': 'title', 'offset': '1', 'limit': '1'})
        queryset = Post.objects.all().order_by('title')[1:2]
        serializer = PostSerializer(queryset, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_request(self):
        response = self.client.get('/posts/', {'order': 'sdf', 'offset': '-1', 'limit': '100000'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(set(response.data.keys()), {'order', 'offset', 'limit'})

