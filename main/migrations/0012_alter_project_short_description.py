# Generated by Django 3.2.3 on 2021-05-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_project_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(max_length=180),
        ),
    ]
