# Generated by Django 3.2.9 on 2022-01-06 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_rename_teacher_department_teacher_deptt'),
        ('course', '0004_attendance_courseclass_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseclass',
            name='teacher',
        ),
        migrations.AddField(
            model_name='courseclass',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher'),
        ),
    ]
