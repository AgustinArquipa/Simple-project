# Generated by Django 5.0.6 on 2024-07-12 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_patrimony_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrimony',
            name='code',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Codigo'),
        ),
    ]
