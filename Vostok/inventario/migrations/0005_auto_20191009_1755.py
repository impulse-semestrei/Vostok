# Generated by Django 2.2.6 on 2019-10-09 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20191009_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fechaMod',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]