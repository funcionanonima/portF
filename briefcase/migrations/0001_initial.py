# Generated by Django 2.1.8 on 2019-06-29 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment', models.CharField(max_length=100)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('company', models.CharField(max_length=50)),
                ('show', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencia',
            },
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gradedate', models.DateField()),
                ('school', models.CharField(max_length=50)),
                ('show', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
            },
        ),
    ]
