# Generated by Django 2.2 on 2019-04-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoremng', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='course_number',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='student_number',
            new_name='student_id',
        ),
    ]
