# Generated by Django 3.2.3 on 2021-07-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_project_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]