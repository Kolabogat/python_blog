from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    IntegerField,
    ForeignKey,
    PROTECT,
    BooleanField,
    TextField,
    ManyToManyField,
)
from django.urls import reverse
from django.contrib.auth.models import User


DIFFICULTIES = [
    ('easy', 'Easy'),
    ('average', 'Average'),
    ('hard', 'Hard'),
    ('very_hard', 'Very Hard'),
]

THEMES = [
    ('python', 'Python'),
    ('libraries', 'Libraries'),
    ('databases', 'Databases'),
    ('deploy', 'Deploy'),
    ('theory', 'Theory'),
    ('algorithms', 'Algorithms'),
]


class Article(Model):
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['id']

    user = ForeignKey(User, verbose_name='User', on_delete=PROTECT, related_name='user_article')
    title = CharField(max_length=75, verbose_name='Title', unique=True)
    content = TextField(verbose_name='Content')
    theme = CharField(max_length=50, choices=THEMES, verbose_name='Theme', default='python')
    words_number = IntegerField(verbose_name='Number of Words', default=0)
    difficulty = CharField(max_length=50, choices=DIFFICULTIES, verbose_name='Difficulty', default='average')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified_at = DateTimeField(auto_now=True, verbose_name='Modified at')
    is_published = BooleanField(verbose_name='Published', default=True)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.title)


class ArticleViewers(Model):
    class Meta:
        verbose_name = 'Viewers of Article'
        ordering = ['id']

    article = ForeignKey(Article, verbose_name='Article', on_delete=PROTECT, related_name='article_viewers')
    viewers = ManyToManyField(User, verbose_name='Viewers')

    def __str__(self):
        return str(self.article)
