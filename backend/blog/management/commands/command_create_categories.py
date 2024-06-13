from django.core.management.base import BaseCommand

from ..categories import CATEGORIES
from ...models import Categories


class Command(BaseCommand):
    help = """
    Command that uploads constants that are needed for user settings
    """

    def handle(self, *args, **options):
        for category_dict in CATEGORIES:
            category = category_dict.get('category')
            if not Categories.objects.filter(
                    pk=category_dict.get('id'),
                    category=category
            ):
                category_model = Categories(**category_dict)
                category_model.save()
                self.stdout.write(f'Category: "{category}" added or changed.')
            else:
                self.stdout.write(f'Category: "{category}" already exist.')

        return self.stdout.write(f'Completed: command_create_categories')
