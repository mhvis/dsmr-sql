from datetime import datetime

from django.db import models
from dsmr_parser.objects import Telegram


class TelegramRaw(models.Model):
    """Raw telegram strings."""
    time = models.DateTimeField(primary_key=True)
    telegram = models.TextField()


class ElectricityReading(models.Model):
    """Electricity consumption or return in kWh and current power usage in kW."""
    time = models.DateTimeField(primary_key=True)
    used_1 = models.DecimalField(max_digits=9, decimal_places=3)
    used_2 = models.DecimalField(max_digits=9, decimal_places=3)
    delivered_1 = models.DecimalField(max_digits=9, decimal_places=3)
    delivered_2 = models.DecimalField(max_digits=9, decimal_places=3)
    current_usage = models.DecimalField(null=True, max_digits=9, decimal_places=3)
    current_delivery = models.DecimalField(null=True, max_digits=9, decimal_places=3)


class GasReading(models.Model):
    """Gas meter reading in m3."""
    time = models.DateTimeField(primary_key=True)
    value = models.DecimalField(max_digits=9, decimal_places=3)


def save_telegram(telegram: Telegram, time: datetime):
    """Save a dsmr_parser Telegram object in the database."""

    # Could put this in an atomic transaction but is probably not really necessary

    # Using create instead of save ensures that IntegrityError is raised when time already exists
    TelegramRaw.objects.create(
        time=time,
        telegram=telegram._telegram_data
    )
    ElectricityReading.objects.create(
        time=time,
        used_1=telegram.ELECTRICITY_USED_TARIFF_1.value,
        used_2=telegram.ELECTRICITY_USED_TARIFF_2.value,
        delivered_1=telegram.ELECTRICITY_DELIVERED_TARIFF_1.value,
        delivered_2=telegram.ELECTRICITY_DELIVERED_TARIFF_2.value,
        current_usage=telegram.CURRENT_ELECTRICITY_USAGE.value,
        current_delivery=telegram.CURRENT_ELECTRICITY_DELIVERY.value
    )
    try:
        gas = telegram.HOURLY_GAS_METER_READING
    except KeyError:
        try:
            gas = telegram.GAS_METER_READING
        except KeyError:
            gas = None
    if gas:
        # This should raise IntegrityError if the same timestamp already exists but with a different value
        GasReading.objects.get_or_create(
            time=gas.datetime,
            value=gas.value,
        )
