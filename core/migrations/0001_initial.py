# Generado por Django 5.2.12
# Este archivo es una MIGRACIÓN.
# Django usa este archivo para definir cómo crear las tablas en la base de datos.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    # 'initial = True' indica que esta es la primera migración de la app.
    initial = True

    # 'dependencies' lista las migraciones de las que depende esta.
    # Está vacía porque es la primera.
    dependencies = [
    ]

    # 'operations' contiene la lista de instrucciones SQL que Django ejecutará.
    operations = [
        # Operación 1: Crear el modelo (tabla) Doctor
        migrations.CreateModel(
            name='Doctor',
            fields=[
                # Clave Primaria (ID) autogenerada
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
        # Operación 2: Crear el modelo (tabla) Paciente
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        # Operación 3: Crear el modelo (tabla) CitaMedica con claves foráneas
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('motivo', models.TextField()),
                # Relaciones ForeignKey (Muchos a Uno)
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
    ]
