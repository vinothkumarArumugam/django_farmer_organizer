# Generated by Django 4.2.4 on 2023-12-20 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0006_alter_farmermodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmermodel',
            name='farmer_name',
        ),
    ]
