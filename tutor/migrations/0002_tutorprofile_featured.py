# Generated by Django 3.2.7 on 2021-09-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorprofile',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
