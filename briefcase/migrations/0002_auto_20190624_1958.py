# Generated by Django 2.1.8 on 2019-06-25 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briefcase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studies',
            old_name='fechagrado',
            new_name='gradedate',
        ),
        migrations.RenameField(
            model_name='studies',
            old_name='institucion',
            new_name='school',
        ),
    ]
