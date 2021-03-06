from django.core.management.base import BaseCommand

from core.utils import parse_files


class Command(BaseCommand):
    help = 'Import words'

    def handle(self, *args, **options):
        for i, word in enumerate(parse_files()):
            if i % 10 == 0:
                print(i, word)
        self.stdout.write(self.style.SUCCESS('Successfully imported words'))
