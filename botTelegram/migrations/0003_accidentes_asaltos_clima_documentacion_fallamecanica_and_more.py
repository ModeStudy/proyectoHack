# Generated by Django 5.0.2 on 2024-04-20 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botTelegram', '0002_trafico_fecha_trafico_intensidadtrafico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accidentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.CharField(max_length=200)),
                ('GravedadAccidente', models.IntegerField(default=0)),
                ('Fecha', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Asaltos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.CharField(max_length=200)),
                ('Fecha', models.DateTimeField(default=None)),
                ('PerdidasEconomicas', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('IsAsaltoArmado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.CharField(max_length=200)),
                ('TipoClima', models.CharField(max_length=50)),
                ('Fecha', models.DateTimeField(default=None)),
                ('IsNecesidadHotel', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(default=None)),
                ('TipoDocumentacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FallaMecanica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.CharField(max_length=200)),
                ('Fecha', models.DateTimeField(default=None)),
                ('Falla', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gasolina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PorcentajeGasolina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('DineroDisponible', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Ubicacion', models.CharField(max_length=200)),
                ('Fecha', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='Accidente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botTelegram.accidentes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='Asalto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botTelegram.asaltos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='CLima',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botTelegram.clima'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='Documentacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botTelegram.documentacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='FalloMecanico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botTelegram.fallamecanica'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='Gas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botTelegram.gasolina'),
            preserve_default=False,
        ),
    ]
