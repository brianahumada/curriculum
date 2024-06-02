# Generated by Django 5.0.6 on 2024-05-30 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_personalinfo_github_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='resume.personalinfo')),
            ],
        ),
    ]