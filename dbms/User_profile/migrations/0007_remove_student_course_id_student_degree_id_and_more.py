# Generated by Django 5.0.4 on 2024-04-28 20:01

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_profile', '0006_alter_profile_last_login_alter_student_course_id'),
        ('acadamic', '0004_alter_courses_degree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course_id',
        ),
        migrations.AddField(
            model_name='student',
            name='degree_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acadamic.degree', verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 1, 31, 19, 796698), verbose_name='last login'),
        ),
    ]
