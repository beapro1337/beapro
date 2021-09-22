# Generated by Django 3.2.7 on 2021-09-22 18:40

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
            name='TutorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=55)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('collegeName', models.CharField(blank=True, max_length=60)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('about_me', models.TextField(max_length=300)),
                ('experience', models.TextField(max_length=300)),
                ('subject', models.CharField(choices=[('Mathematics', 'Mathematics'), ('History', 'History'), ('Programming', 'Programming'), ('Art', 'Art'), ('Music', 'Music'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Languages', 'Languages')], default=None, max_length=20, null=True)),
                ('individual', models.BooleanField(default=False)),
                ('group', models.BooleanField(default=False)),
                ('class_will_be_held_on', models.CharField(choices=[('Online', 'Online'), ('Your Home', 'Your Home'), ('At my home', 'At my home')], default=None, max_length=20, null=True)),
                ('your_cv', models.FileField(upload_to='tutor/documents/cv/%Y-%m-%d')),
                ('qualification', models.CharField(max_length=35)),
                ('qualification_cert', models.FileField(upload_to='tutor/documents/edu/%Y-%m-%d')),
                ('amount', models.IntegerField(default=100)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
