# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-13 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante_comandas', '0002_auto_20170309_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesas',
            name='cmesa',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meseros',
            name='cmero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]