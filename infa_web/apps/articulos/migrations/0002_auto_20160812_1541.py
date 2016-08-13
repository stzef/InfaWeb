# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arlo',
            name='cubica',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='base.Ubica'),
        ),
        migrations.AlterField(
            model_name='arlo',
            name='foto1',
            field=models.FileField(blank=True, default=b'static/img/articles/default.jpg', null=True, upload_to='img/articles/'),
        ),
        migrations.AlterField(
            model_name='arlo',
            name='foto2',
            field=models.FileField(blank=True, default=b'static/img/articles/default.jpg', null=True, upload_to='img/articles/'),
        ),
        migrations.AlterField(
            model_name='arlo',
            name='foto3',
            field=models.FileField(blank=True, default=b'static/img/articles/default.jpg', null=True, upload_to='img/articles/'),
        ),
    ]