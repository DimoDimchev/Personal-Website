# Generated by Django 3.2.3 on 2021-05-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='short_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
