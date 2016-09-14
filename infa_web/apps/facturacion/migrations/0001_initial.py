# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 15:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        ('base', '0001_initial'),
        ('terceros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfac', models.CharField(max_length=10)),
                ('femi', models.DateTimeField()),
                ('fpago', models.DateTimeField()),
                ('descri', models.CharField(max_length=200)),
                ('detaanula', models.CharField(max_length=200)),
                ('vtbase', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vtiva', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vflete', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vdescu', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vttotal', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vefe', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vtar', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('doctar', models.CharField(max_length=10)),
                ('vchq', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('docchq', models.CharField(max_length=10)),
                ('ventre', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vcambio', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('tpordes', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('vncre', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('doccre', models.CharField(max_length=10)),
                ('brtefte', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('prtefte', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('vrtefte', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('fhasdomi', models.DateTimeField()),
                ('bancochq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bancochq', to='base.Banfopa')),
                ('bancotar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bancotar', to='base.Banfopa')),
                ('ccaja', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Caja')),
                ('cdomici', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Domici')),
                ('cemdor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Emdor')),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
                ('citerce', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='terceros.Tercero')),
                ('ctifopa', models.ForeignKey(default=1001, on_delete=django.db.models.deletion.CASCADE, to='base.Tifopa')),
                ('cvende', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='terceros.Vende')),
            ],
        ),
        migrations.CreateModel(
            name='Facdeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itfac', models.CharField(max_length=4)),
                ('nlargo', models.CharField(max_length=100)),
                ('ncorto', models.CharField(max_length=20)),
                ('canti', models.DecimalField(decimal_places=2, default=1, max_digits=16, validators=[django.core.validators.MinValueValidator(0)])),
                ('niva', models.CharField(max_length=40)),
                ('poriva', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('vunita', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vbase', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('viva', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vtotal', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('pordes', models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvtafull', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('vcosto', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('carlos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.Arlo')),
                ('cfac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Fac')),
                ('civa', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Iva')),
            ],
        ),
    ]
