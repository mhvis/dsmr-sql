from django.db import models


class Telegram(models.Model):
    time = models.DateTimeField()

    # Raw telegram string
    raw = models.TextField()

    # Parsed values
    electricity_used_tariff_1 = models.DecimalField(max_digits=10, decimal_places=3)
    electricity_used_tariff_2 = models.DecimalField(max_digits=10, decimal_places=3)
    electricity_delivered_tariff_1 = models.DecimalField(max_digits=10, decimal_places=3)
    electricity_delivered_tariff_2 = models.DecimalField(max_digits=10, decimal_places=3)
    electricity_active_tariff = models.CharField(max_length=100)
    current_electricity_usage = models.DecimalField(max_digits=10, decimal_places=3)
    current_electricity_delivery = models.DecimalField(max_digits=10, decimal_places=3)
    gas_meter_time = models.DateTimeField()
    gas_meter_reading = models.DecimalField(max_digits=10, decimal_places=3)

    @classmethod
    def from_object(cls, telegram):
        """Create instance from Telegram objects from dsmr_parser library."""
        return cls(
            time=telegram.P1_MESSAGE_TIMESTAMP.value,
            raw=telegram._telegram_data,
            electricity_used_tariff_1=telegram.ELECTRICITY_USED_TARIFF_1.value,

        )
