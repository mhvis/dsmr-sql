import logging

from django.conf import settings
from django.core.management import BaseCommand
from dsmr_parser.clients import SerialReader

from dsmrsql.models import Telegram

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'DSMR logger'

    def handle(self, *args, **options):
        serial_reader = SerialReader(
            device=settings.DSMR_DEVICE,
            serial_settings=settings.DSMR_SERIAL_SETTINGS,
            telegram_specification=settings.DSMR_TELEGRAM_SPECIFICATION,
        )

        for telegram in serial_reader.read_as_object():
            Telegram.from_object(telegram).save()
