# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),
        ('terceros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('finusu', models.DateTimeField()),
                ('fveusu', models.DateTimeField()),
                ('foto', models.ImageField(upload_to='usuarios/')),
                ('ifprises', models.BooleanField()),
                ('ccaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Caja')),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
                ('cvende', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Vende')),
            ],
        ),
    ]