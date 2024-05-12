# Generated by Django 5.0.4 on 2024-05-12 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NMX_R_025_SCFI_2015', '0002_rename_message_logmessage_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giro', models.CharField(max_length=9)),
                ('actividad', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='LogEval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('sector', models.CharField(choices=[('PU', 'Público'), ('PR', 'Privado'), ('SO', 'Social')], max_length=2, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector_productivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamaño', models.CharField(max_length=7)),
                ('sector_productivo', models.CharField(max_length=21, unique=True)),
                ('cant_personal', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ct', models.CharField(max_length=300)),
                ('razon_social', models.CharField(max_length=20)),
                ('rfc', models.CharField(max_length=50)),
                ('equipo_seguridad_descripcion', models.TextField(max_length=300)),
                ('adicional_logistica', models.TextField(max_length=200)),
                ('multisitio', models.BooleanField(default=False)),
                ('id_giro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.giro')),
                ('id_sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.sector')),
                ('id_sector_productivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.sector_productivo')),
            ],
        ),
    ]
