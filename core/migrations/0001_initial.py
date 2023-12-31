# Generated by Django 4.2.2 on 2023-06-25 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=50, verbose_name='Especialidad')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
            ],
            options={
                'verbose_name': 'especialidad',
                'verbose_name_plural': 'especialidades',
                'ordering': ['specialization'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Asignatura')),
                ('semester', models.IntegerField(verbose_name='Semestre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specialization', verbose_name='Especialidad')),
            ],
            options={
                'verbose_name': 'asignatura',
                'verbose_name_plural': 'asignaturas',
                'ordering': ['subject'],
            },
        ),
    ]
