import requests
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup

from hacker_news_posts.models import Post


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        self.stdout.write(self.style.NOTICE('Upload from https://news.ycombinator.com/'))

        response = requests.get('https://news.ycombinator.com/')
        soup = BeautifulSoup(response.content, "html.parser")

        links = soup.find_all('a', {'class': 'storylink'})

        for link in links:
            url = link.attrs['href']
            title = link.text

            Post.objects.create(title=title, url=url)

        self.stdout.write(self.style.SUCCESS('Loading is complete'))
