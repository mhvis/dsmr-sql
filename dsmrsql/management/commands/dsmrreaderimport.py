from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Import readings from DSMR-reader using its API."

    def add_arguments(self, parser):
        parser.add_argument('api_url', help="The base URL of the DSMR-reader installation, e.g. https://example.com.")
        parser.add_argument('api_key', help="The API key set in the configuration.")

    def handle(self, *args, **options):
        pass
