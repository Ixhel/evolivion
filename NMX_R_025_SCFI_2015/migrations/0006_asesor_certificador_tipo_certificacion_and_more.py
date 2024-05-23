# Generated by Django 5.0.4 on 2024-05-15 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NMX_R_025_SCFI_2015', '0005_alter_sector_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor_certificador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('registro', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_certificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('INICIAL', 'Inicial'), ('VIGILANCIA', 'Vigilancia'), ('RENOVACION', 'Renovacion')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='sector_productivo',
            name='cant_personal',
            field=models.CharField(choices=[('0 a 10', '0 a 10'), ('11 a 30', '11 a 30'), ('11 a 50', '11 a 50'), ('31 a 100', '31 a 100'), ('51 a 100', '51 a 100'), ('51 a 250', '51 a 250'), ('251 en adelante', '251 en adelante')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sector_productivo',
            name='sector_productivo',
            field=models.CharField(choices=[('TODO', 'Todo'), ('COMERCIO', 'Comercio'), ('INDUSTRIA Y SERVICIOS', 'Industria y Servicios'), ('SERVICIOS', 'Servicios'), ('INDUSTRIA', 'Industria')], max_length=25),
        ),
        migrations.AlterField(
            model_name='sector_productivo',
            name='tamaño',
            field=models.CharField(choices=[('MICRO', 'Micro'), ('PEQUEÑA', 'Pequeña'), ('MEDIANA', 'Mediana'), ('GRANDE', 'Grande')], max_length=7),
        ),
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('id_asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.asesor_certificador')),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_certificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.certificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio_empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=50)),
                ('del_mun', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Encargado_ct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=25)),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='certificacion',
            name='id_ecargado_ct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.encargado_ct'),
        ),
        migrations.CreateModel(
            name='Multisitio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=50)),
                ('del_mun', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('id_domicilio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.domicilio_empresa')),
            ],
        ),
        migrations.AddField(
            model_name='certificacion',
            name='id_tipo_cert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NMX_R_025_SCFI_2015.tipo_certificacion'),
        ),
    ]
