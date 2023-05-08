# Generated by Django 4.2.1 on 2023-05-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Beer name')),
                ('brewery', models.CharField(max_length=255, verbose_name='Brewery name')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Beer price')),
                ('photo', models.FileField(upload_to='%Y/%m/%d/', verbose_name='Company photo')),
                ('fortress', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Beer fortress')),
            ],
            options={
                'verbose_name': 'Пиво (Beer)',
                'verbose_name_plural': 'Beers',
            },
        ),
    ]
