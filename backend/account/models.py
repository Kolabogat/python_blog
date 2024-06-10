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

from backend.utils import get_account_image_path, get_default_account_image_path

GENDERS = [
    ('unknown', 'Unknown'),
    ('female', 'Female'),
    ('male', 'Male'),
]


class UserProfile(Model):
    class Meta:
        verbose_name = 'User Profile'
        ordering = ['user']

    user = ForeignKey(User, verbose_name='User', on_delete=PROTECT, related_name='user_profile')
    image = ImageField(upload_to=get_account_image_path, verbose_name='Image', default=get_default_account_image_path())
    name = CharField(max_length=50, verbose_name='Name', blank=True)
    gender = CharField(max_length=50, verbose_name='Gender', choices=GENDERS, default='unknown')
    date_of_birth = DateTimeField(verbose_name='Date of Birth', blank=True, null=True)
    about = CharField(max_length=100, verbose_name='About User', blank=True)
    address = CharField(max_length=50, verbose_name='Address', blank=True)
    email = EmailField(verbose_name='E-mail', blank=True,)

    def __str__(self):
        return str(self.user)
