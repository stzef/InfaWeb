# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-02 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_sucursales'),
    ]

    operations = [
        migrations.AddField(
            model_name='talo',
            name='csucur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Sucursales'),
        ),
    ]