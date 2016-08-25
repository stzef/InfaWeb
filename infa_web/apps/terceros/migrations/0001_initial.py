# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-24 14:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorre',
            fields=[
                ('cautorre', models.AutoField(primary_key=True, serialize=False)),
                ('nautorre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('cpersona', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('npersona', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('cruta', models.AutoField(primary_key=True, serialize=False)),
                ('nruta', models.CharField(max_length=45)),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('citerce', models.AutoField(primary_key=True, serialize=False)),
                ('idterce', models.CharField(max_length=20)),
                ('dv', models.CharField(max_length=1)),
                ('rasocial', models.CharField(max_length=200)),
                ('nomcomer', models.CharField(max_length=200)),
                ('ape1', models.CharField(max_length=40)),
                ('ape2', models.CharField(max_length=40)),
                ('nom1', models.CharField(max_length=40)),
                ('nom2', models.CharField(max_length=40)),
                ('sigla', models.CharField(max_length=100)),
                ('replegal', models.CharField(max_length=100)),
                ('dirterce', models.CharField(max_length=80)),
                ('telterce', models.CharField(max_length=20)),
                ('faxterce', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('contacto', models.CharField(max_length=20)),
                ('topcxc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('clipre', models.IntegerField(default=1)),
                ('fnaci', models.DateField(default=django.utils.timezone.now)),
                ('ordenruta', models.IntegerField()),
                ('cautorre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Autorre')),
                ('cesdo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Ciudad')),
                ('cpersona', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='terceros.Personas')),
                ('cregiva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Regiva')),
                ('cruta', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='terceros.Ruta')),
                ('ctiide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Tiide')),
            ],
        ),
        migrations.CreateModel(
            name='Vende',
            fields=[
                ('cvende', models.AutoField(primary_key=True, serialize=False)),
                ('nvende', models.CharField(max_length=80)),
                ('porventa', models.DecimalField(decimal_places=4, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('czona', models.AutoField(primary_key=True, serialize=False)),
                ('nzona', models.CharField(max_length=40)),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.AddField(
            model_name='tercero',
            name='cvende',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Vende'),
        ),
        migrations.AddField(
            model_name='tercero',
            name='czona',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='terceros.Zona'),
        ),
    ]
