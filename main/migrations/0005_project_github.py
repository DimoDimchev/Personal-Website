# Generated by Django 3.2.3 on 2021-05-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_blogpost_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
