# Generated by Django 4.2.1 on 2023-05-06 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0005_alter_beer_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='photo',
        ),
    ]
