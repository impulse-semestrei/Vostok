# Generated by Django 2.2.6 on 2019-10-22 18:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20191022_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fecha_mod',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 18, 24, 43, 853518, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='inventariomaterial',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 18, 24, 43, 853518, tzinfo=utc)),
        ),
    ]
