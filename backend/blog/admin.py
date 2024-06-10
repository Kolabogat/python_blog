from django.contrib import admin

from blog.models import Article, ArticleViewers, Categories, Difficulties

admin.site.register(Article)
admin.site.register(ArticleViewers)
admin.site.register(Categories)
admin.site.register(Difficulties)
