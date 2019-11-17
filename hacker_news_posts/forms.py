from django import forms
from django.core.exceptions import ValidationError

from hacker_news_posts.models import Post


class ParamsForm(forms.Form):
    order = forms.CharField(required=False)
    offset = forms.IntegerField(min_value=0, required=False)
    limit = forms.IntegerField(min_value=0, max_value=1000, required=False)

    def clean_order(self):
        value = self.cleaned_data['order']
        fields = list(map(lambda x: x.name, Post._meta.get_fields()))
        if value and value not in fields:
            raise ValidationError(f'Available for order fields: {", ".join(fields)}')
        return value
