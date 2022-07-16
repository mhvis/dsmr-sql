# Generated by Django 4.0.6 on 2022-07-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsmrsql', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegram',
            name='current_electricity_delivery',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='current_electricity_usage',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='electricity_delivered_tariff_1',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='electricity_delivered_tariff_2',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='electricity_used_tariff_1',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='electricity_used_tariff_2',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='gas_meter_reading',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='telegram',
            name='gas_meter_time',
            field=models.DateTimeField(null=True),
        ),
    ]