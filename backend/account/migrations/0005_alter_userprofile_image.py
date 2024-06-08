# Generated by Django 5.0.6 on 2024-06-05 16:45

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default/image/default.jpg', upload_to=account.models.get_image_path, verbose_name='Image'),
        ),
    ]