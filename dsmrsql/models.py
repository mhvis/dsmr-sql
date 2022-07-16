from django.db import models


class Telegram(models.Model):
    time = models.DateTimeField()

    # Raw telegram string
    raw = models.TextField()

    # Parsed values
    electricity_used_tariff_1 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    electricity_used_tariff_2 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    electricity_delivered_tariff_1 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    electricity_delivered_tariff_2 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    electricity_active_tariff = models.CharField(max_length=100)
    current_electricity_usage = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    current_electricity_delivery = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    gas_meter_time = models.DateTimeField(null=True)
    gas_meter_reading = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    @classmethod
    def from_object(cls, telegram, time=None):
        """Create instance from Telegram objects from dsmr_parser library.

        Args:
            telegram: A dsmr_parser Telegram object.
            time: If given, will be used as time instead of the telegram timestamp.
        """
        return cls(
            time=time or telegram.P1_MESSAGE_TIMESTAMP.value,
            raw=telegram._telegram_data,
            electricity_used_tariff_1=telegram.ELECTRICITY_USED_TARIFF_1.value,
            electricity_used_tariff_2=telegram.ELECTRICITY_USED_TARIFF_2.value,
            electricity_delivered_tariff_1=telegram.ELECTRICITY_DELIVERED_TARIFF_1.value,
            electricity_delivered_tariff_2=telegram.ELECTRICITY_DELIVERED_TARIFF_2.value,
        )
