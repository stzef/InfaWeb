# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('facturacion', '0001_initial'),
        ('terceros', '0001_initial'),
        ('articulos', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rue',
            name='cusu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='facdeta',
            name='carlos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.Arlo'),
        ),
        migrations.AddField(
            model_name='facdeta',
            name='cfac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Fac'),
        ),
        migrations.AddField(
            model_name='fac',
            name='bancochq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bancochq', to='base.Banfopa'),
        ),
        migrations.AddField(
            model_name='fac',
            name='bancotar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bancotar', to='base.Banfopa'),
        ),
        migrations.AddField(
            model_name='fac',
            name='ccaja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Caja'),
        ),
        migrations.AddField(
            model_name='fac',
            name='cdomici',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Domici'),
        ),
        migrations.AddField(
            model_name='fac',
            name='cemdor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Emdor'),
        ),
        migrations.AddField(
            model_name='fac',
            name='cesdo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo'),
        ),
        migrations.AddField(
            model_name='fac',
            name='citerce',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='terceros.Tercero'),
        ),
        migrations.AddField(
            model_name='fac',
            name='ctifopa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Tifopa'),
        ),
        migrations.AddField(
            model_name='fac',
            name='cvende',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='terceros.Vende'),
        ),
    ]
