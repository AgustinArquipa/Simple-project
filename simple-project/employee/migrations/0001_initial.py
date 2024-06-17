# Generated by Django 5.0.6 on 2024-06-17 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=60, null=True, verbose_name='Apellido y Nombre')),
                ('dni', models.CharField(blank=True, db_index=True, max_length=10, null=True, verbose_name='Documento')),
                ('gruoping', models.CharField(blank=True, max_length=25, null=True, verbose_name='Agrupamiento')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Direccion')),
                ('service', models.CharField(blank=True, max_length=100, null=True, verbose_name='Servicio')),
                ('status', models.CharField(blank=True, choices=[('Monotributo', 'Monotributo'), ('Planta', 'Planta'), ('Planta Trans.', 'Planta Trans'), ('Contratado', 'Contratado')], default='Planta', null=True, verbose_name='Sit. Laboral')),
                ('box', models.CharField(blank=True, max_length=15, null=True, verbose_name='Taquilla')),
                ('asset_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='N° Patrimonial')),
                ('unit', models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='Cantidad Unitaria')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ubicacion')),
                ('code', models.CharField(blank=True, max_length=30, null=True, verbose_name='Codigo')),
            ],
            options={
                'db_table': 'Empleado',
            },
        ),
    ]