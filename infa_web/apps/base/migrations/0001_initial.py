# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('cciu', models.AutoField(primary_key=True, serialize=False)),
                ('nciu', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('cdepar', models.AutoField(primary_key=True, serialize=False)),
                ('ndepar', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Esdo',
            fields=[
                ('cesdo', models.AutoField(primary_key=True, serialize=False)),
                ('nesdo', models.CharField(max_length=40)),
                ('estavali', models.CharField(max_length=10)),
                ('colfon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('civa', models.AutoField(primary_key=True, serialize=False)),
                ('niva', models.CharField(max_length=40)),
                ('poriva', models.DecimalField(decimal_places=2, max_digits=6)),
                ('idtira', models.CharField(max_length=1)),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Regiva',
            fields=[
                ('cregiva', models.AutoField(primary_key=True, serialize=False)),
                ('nregiva', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tiide',
            fields=[
                ('idtiide', models.AutoField(primary_key=True, serialize=False)),
                ('ntiide', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ubica',
            fields=[
                ('cubica', models.AutoField(primary_key=True, serialize=False)),
                ('nubica', models.CharField(max_length=80)),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='cdepar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Departamento'),
        ),
    ]
