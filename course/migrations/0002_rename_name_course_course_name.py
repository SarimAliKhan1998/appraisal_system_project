# Generated by Django 3.2.9 on 2021-12-14 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
    ]
