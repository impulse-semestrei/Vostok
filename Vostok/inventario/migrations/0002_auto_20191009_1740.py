# Generated by Django 2.2.6 on 2019-10-09 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fechaMod',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]