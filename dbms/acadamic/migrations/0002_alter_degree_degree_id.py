# Generated by Django 5.0.4 on 2024-04-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acadamic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='degree_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='course id'),
        ),
    ]
