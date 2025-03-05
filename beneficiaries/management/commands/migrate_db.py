from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs database migrations'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Running makemigrations...'))
        call_command('makemigrations')
        self.stdout.write(self.style.SUCCESS('Running migrate...'))
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Database migrations completed.'))