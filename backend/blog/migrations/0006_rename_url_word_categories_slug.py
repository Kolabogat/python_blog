# Generated by Django 5.0.6 on 2024-06-11 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_categories_category_alter_categories_url_word'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='url_word',
            new_name='slug',
        ),
    ]