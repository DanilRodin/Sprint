# Generated by Django 4.2.4 on 2023-09-15 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0007_levels_delete_perevalareas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevaladded',
            old_name='author',
            new_name='user',
        ),
    ]
