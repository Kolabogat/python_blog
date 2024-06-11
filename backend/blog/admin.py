from django.contrib import admin

from blog.models import Article, ArticleViewers, Categories, Difficulties


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}


admin.site.register(Article)
admin.site.register(ArticleViewers)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Difficulties)
