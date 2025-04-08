from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Check if DEBUG is True or False'

    def handle(self, *args, **options):
        debug_status = settings.DEBUG
        status = 'ON' if debug_status else 'OFF'
        self.stdout.write(self.style.SUCCESS(f'DEBUG is {status}'))
