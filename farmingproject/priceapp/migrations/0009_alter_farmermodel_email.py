# Generated by Django 4.2.4 on 2023-12-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0008_alter_farmermodel_options_alter_farmermodel_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmermodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
