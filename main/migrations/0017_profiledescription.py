# Generated by Django 3.2.3 on 2021-12-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_project_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField()),
            ],
        ),
    ]