import os
import uuid
from django.contrib.auth.models import User


def get_file_path(instance, filename, directory):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(f'account/{instance.user}/{directory}/', filename)


def get_account_image_path(instance, filename):
    return get_file_path(
        instance=instance,
        filename=filename,
        directory="avatar"
    )


def get_default_account_image_path():
    return os.path.join(f'default/avatar/default.png')


def get_blog_image_path(instance, filename):
    return get_file_path(
        instance=instance,
        filename=filename,
        directory="blog"
    )


def get_admin_id():
    return User.objects.get(username='admin').id
