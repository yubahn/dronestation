# Generated by Django 4.2.7 on 2023-11-14 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0004_flightdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightdata',
            name='battery_voltage',
            field=models.FloatField(default=0),
        ),
    ]