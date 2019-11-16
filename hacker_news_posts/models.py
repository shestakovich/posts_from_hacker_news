from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=1024)
    url = models.URLField('URL')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if len(self.title) < 30 else f'{self.title[:30]}...'

    class Meta:
        db_table = 'post'
        ordering = ['-created']