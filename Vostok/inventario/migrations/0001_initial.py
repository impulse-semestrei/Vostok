# Generated by Django 2.2.6 on 2019-10-23 15:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('fecha_mod', models.DateTimeField(default=datetime.datetime(2019, 10, 23, 15, 54, 20, 856579, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='InventarioMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Inventario')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material')),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='materiales',
            field=models.ManyToManyField(through='inventario.InventarioMaterial', to='material.Material'),
        ),
    ]
