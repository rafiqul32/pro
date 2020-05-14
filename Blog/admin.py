from django.contrib import admin
from .models import Article


class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'content')


admin.site.register(Article, BlogAdmin)