# Generated by Django 2.2.6 on 2019-10-23 16:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20191023_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fecha_mod',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 23, 16, 15, 41, 433877, tzinfo=utc)),
        ),
    ]
