# Generated by Django 5.0.6 on 2024-06-28 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_condition'),
        ('lockers', '0002_locker_patrimony_alter_locker_status_locker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lockers', to='employee.employee', verbose_name='Empleado'),
        ),
    ]
