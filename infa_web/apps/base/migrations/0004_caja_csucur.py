# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-02 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_talo_csucur'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='csucur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Sucursales'),
        ),
    ]