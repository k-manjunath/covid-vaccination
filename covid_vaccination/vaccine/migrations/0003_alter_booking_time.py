# Generated by Django 4.1.4 on 2022-12-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
