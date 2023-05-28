# Generated by Django 4.2.1 on 2023-05-28 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('body', models.TextField(max_length=2500)),
            ],
        ),
    ]
