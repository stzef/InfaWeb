# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-21 11:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banfopa',
            fields=[
                ('cbanfopa', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nbanfopa', models.CharField(max_length=80)),
                ('porcomi', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Bode',
            fields=[
                ('cbode', models.AutoField(primary_key=True, serialize=False)),
                ('nbode', models.CharField(max_length=80)),
                ('esbode', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('ccaja', models.AutoField(primary_key=True, serialize=False)),
                ('ncaja', models.CharField(max_length=80)),
                ('caseri', models.CharField(max_length=4)),
                ('cbode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Bode')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('cciu', models.AutoField(primary_key=True, serialize=False)),
                ('nciu', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Cta',
            fields=[
                ('ccta', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ncta', models.CharField(max_length=80)),
                ('natu', models.IntegerField()),
                ('ifbase', models.BooleanField()),
                ('ifterce', models.BooleanField()),
                ('ifcencos', models.BooleanField()),
                ('ifajus', models.BooleanField()),
                ('ifestas', models.BooleanField()),
                ('ifrtefte', models.BooleanField()),
                ('prf', models.IntegerField()),
                ('nivel', models.IntegerField()),
                ('timaux', models.IntegerField()),
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
            name='Domici',
            fields=[
                ('cdomici', models.AutoField(primary_key=True, serialize=False)),
                ('ndomici', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Emdor',
            fields=[
                ('cemdor', models.AutoField(primary_key=True, serialize=False)),
                ('nemdor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Esdo',
            fields=[
                ('cesdo', models.AutoField(primary_key=True, serialize=False)),
                ('nesdo', models.CharField(max_length=40)),
                ('estavali', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('civa', models.AutoField(primary_key=True, serialize=False)),
                ('niva', models.CharField(max_length=40)),
                ('poriva', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('idtira', models.CharField(max_length=1)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='MediosPago',
            fields=[
                ('cmpago', models.AutoField(primary_key=True, serialize=False)),
                ('nmpago', models.CharField(max_length=40)),
                ('ifdoc', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smodule', models.CharField(max_length=5)),
                ('nmodule', models.CharField(max_length=20)),
                ('enabled_enterprise', models.BooleanField()),
                ('enabled', models.BooleanField()),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cparam', models.CharField(max_length=10)),
                ('nparam', models.CharField(max_length=40)),
                ('val_boolean', models.BooleanField()),
                ('val_integer', models.IntegerField(blank=True, null=True)),
                ('val_string', models.CharField(blank=True, max_length=40, null=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Modules')),
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
            name='Talo',
            fields=[
                ('ctalo', models.AutoField(primary_key=True, serialize=False)),
                ('prefijo', models.CharField(max_length=2)),
                ('conse_ini', models.IntegerField()),
                ('conse_fin', models.IntegerField()),
                ('lar_conse', models.IntegerField()),
                ('resodian', models.CharField(max_length=20)),
                ('nrepo', models.CharField(max_length=10)),
                ('filas', models.IntegerField()),
                ('descri', models.CharField(max_length=40)),
                ('ifmostrado', models.BooleanField()),
                ('ifpos', models.BooleanField()),
                ('prefi_real', models.CharField(max_length=4)),
                ('ncotalo', models.IntegerField()),
                ('ccaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Caja')),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Tifopa',
            fields=[
                ('ctifopa', models.AutoField(primary_key=True, serialize=False)),
                ('ntifopa', models.CharField(max_length=40)),
                ('ndiasfopa', models.IntegerField()),
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
            name='Timo',
            fields=[
                ('ctimo', models.IntegerField(primary_key=True, serialize=False)),
                ('ntimo', models.CharField(max_length=40)),
                ('prefijo', models.CharField(max_length=4)),
                ('filas', models.IntegerField()),
                ('nrepo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tiservi',
            fields=[
                ('ctiservi', models.AutoField(primary_key=True, serialize=False)),
                ('ntiservi', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ubica',
            fields=[
                ('cubica', models.AutoField(primary_key=True, serialize=False)),
                ('nubica', models.CharField(max_length=80)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.AddField(
            model_name='talo',
            name='ctifopa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Tifopa'),
        ),
        migrations.AddField(
            model_name='talo',
            name='ctimomvsa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Timo'),
        ),
        migrations.AddField(
            model_name='emdor',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
        migrations.AddField(
            model_name='domici',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
        migrations.AddField(
            model_name='cta',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='cdepar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Departamento'),
        ),
        migrations.AddField(
            model_name='caja',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
        migrations.AddField(
            model_name='caja',
            name='ctimocj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Timo'),
        ),
        migrations.AddField(
            model_name='bode',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
        migrations.AddField(
            model_name='banfopa',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
    ]
