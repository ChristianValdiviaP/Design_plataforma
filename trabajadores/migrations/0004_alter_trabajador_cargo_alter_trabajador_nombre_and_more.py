# Generated by Django 5.0.6 on 2024-06-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajadores', '0003_alter_trabajador_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='cargo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='rut',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
