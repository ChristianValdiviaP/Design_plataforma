# Generated by Django 5.0.6 on 2024-06-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_remove_proyecto_faena_remove_proyecto_nombre_and_more'),
        ('trabajadores', '0004_alter_trabajador_cargo_alter_trabajador_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='trabajadores',
            field=models.ManyToManyField(related_name='proyectos', to='trabajadores.trabajador'),
        ),
    ]
