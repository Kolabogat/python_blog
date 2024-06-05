from django.contrib import admin

from blog.models import Article, ArticleViewers

admin.site.register(Article)
admin.site.register(ArticleViewers)
