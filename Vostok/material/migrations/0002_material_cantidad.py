# Generated by Django 2.2.6 on 2019-10-23 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]