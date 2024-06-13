from django.core.management.base import BaseCommand

from ..articles import ARTICLES
from ...models import Article, Categories, Difficulties


class Command(BaseCommand):
    def handle(self, *args, **options):
        for article_dict in ARTICLES:
            title = article_dict.get('title')
            if not Article.objects.filter(title=title):
                Article.objects.create(
                    title=title,
                    content=article_dict.get('content'),
                    category=Categories.objects.filter(id=article_dict.get('category')).first(),
                    difficulty=Difficulties.objects.filter(id=article_dict.get('difficulty')).first(),
                )
                self.stdout.write(f'Article: "{title}" added or changed.')
            else:
                self.stdout.write(f'Article: "{title}" already exist.')

        return self.stdout.write(f'Completed: optional_command_create_articles')
