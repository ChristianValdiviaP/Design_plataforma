# Generated by Django 5.0.6 on 2024-05-22 19:59

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
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadores.cargo')),
            ],
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
        ),
    ]