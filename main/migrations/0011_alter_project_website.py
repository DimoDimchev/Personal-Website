# Generated by Django 3.2.3 on 2021-05-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_project_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
