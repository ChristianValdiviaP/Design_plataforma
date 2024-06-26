# Generated by Django 5.0.6 on 2024-06-19 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadores.cargo')),
            ],
            options={
                'db_table': 'trabajador',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('fecha_emision', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadores.trabajador')),
            ],
            options={
                'db_table': 'documento',
            },
        ),
    ]
