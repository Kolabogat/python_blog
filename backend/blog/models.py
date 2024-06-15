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
    ImageField,
    SlugField,
)
from django.urls import reverse
from django.contrib.auth.models import User

from backend.utils import get_blog_image_path

DIFFICULTIES = [
    ('easy', 'Easy'),
    ('average', 'Average'),
    ('hard', 'Hard'),
    ('very_hard', 'Very Hard'),
]


class Categories(Model):
    category = CharField(max_length=50, verbose_name='Theme', unique=True)
    slug = SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return str(self.category)


class Difficulties(Model):
    difficulty = CharField(max_length=50, verbose_name='Difficulty')
    class_name = CharField(max_length=25, verbose_name='Class')

    def __str__(self):
        return str(self.difficulty)


class Article(Model):
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']

    user = ForeignKey(User, verbose_name='User', on_delete=PROTECT, related_name='user_article')
    title = CharField(max_length=75, verbose_name='Title', unique=True)
    image = ImageField(upload_to=get_blog_image_path, verbose_name='Image', blank=True)
    content = TextField(verbose_name='Content')
    category = ForeignKey(Categories, verbose_name='Theme', on_delete=PROTECT, related_name='article_category')
    words_number = IntegerField(verbose_name='Number of Words', default=0)
    difficulty = ForeignKey(Difficulties, verbose_name='Difficulty', on_delete=PROTECT, related_name='article_difficulty')
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
