# Generated by Django 4.0.4 on 2022-06-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.TextField(blank=True),
        ),
    ]
