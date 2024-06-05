import os
import uuid

from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    DateTimeField,
    EmailField,
    ImageField,
    PROTECT,
)
from django.contrib.auth.models import User


GENDERS = [
    ('unknown', 'Unknown'),
    ('female', 'Female'),
    ('male', 'Male'),
]


def get_file_path(instance, filename, directory):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(f'account/{instance.user}/{directory}/', filename)


def get_image_path(instance, filename):
    return get_file_path(
        instance=instance,
        filename=filename,
        directory="image"
    )


def get_default_image_path():
    return os.path.join(f'default/image/default.jpg')


class UserProfile(Model):
    class Meta:
        verbose_name = 'User Profile'
        ordering = ['user']

    user = ForeignKey(User, verbose_name='User', on_delete=PROTECT, related_name='user_profile')
    image = ImageField(upload_to=get_image_path, verbose_name='Image', default=get_default_image_path())
    name = CharField(max_length=50, verbose_name='Name', blank=True)
    gender = CharField(max_length=50, verbose_name='Gender', choices=GENDERS, default='unknown')
    date_of_birth = DateTimeField(verbose_name='Date of Birth', blank=True, null=True)
    about = CharField(max_length=100, verbose_name='About User', blank=True)
    address = CharField(max_length=50, verbose_name='Address', blank=True)
    email = EmailField(verbose_name='E-mail', blank=True,)

    def __str__(self):
        return str(self.user)
