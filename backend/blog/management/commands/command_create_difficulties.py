from django.core.management.base import BaseCommand

from ..difficulties import DIFFICULTIES
from ...models import Difficulties


class Command(BaseCommand):
    def handle(self, *args, **options):
        for difficulty_dict in DIFFICULTIES:
            difficulty = difficulty_dict.get('difficulty')
            if not Difficulties.objects.filter(
                    pk=difficulty_dict.get('id'),
                    difficulty=difficulty
            ):
                difficulty_model = Difficulties(**difficulty_dict)
                difficulty_model.save()
                self.stdout.write(f'Difficulty: "{difficulty}" added or changed.')
            else:
                self.stdout.write(f'Difficulty: "{difficulty}" already exist.')

        return self.stdout.write(f'Completed: command_create_difficulties')
