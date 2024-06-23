# Generated by Django 5.0.6 on 2024-06-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='asset_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='box',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='code',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='location',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='unit',
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(blank=True, choices=[('Monotributo', 'Monotributo'), ('Planta', 'Planta'), ('Planta Temporal.', 'Planta Temporal'), ('Contratado', 'Contratado')], default='Planta', null=True, verbose_name='Sit. Laboral'),
        ),
    ]