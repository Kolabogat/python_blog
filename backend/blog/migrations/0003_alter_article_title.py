# Generated by Django 5.0.6 on 2024-06-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_options_article_theme_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=75, unique=True, verbose_name='Title'),
        ),
    ]