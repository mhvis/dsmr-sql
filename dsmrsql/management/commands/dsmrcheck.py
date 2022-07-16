from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Does an integrity check on the parsed values and repairs incorrect values.'
