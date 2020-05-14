from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'header',
            'author',
            'content',
            'active',
        ]