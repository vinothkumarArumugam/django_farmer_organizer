# Generated by Django 4.2.4 on 2023-12-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=100)),
                ('farmer_address', models.CharField(max_length=255)),
                ('farmer_district', models.CharField(max_length=100)),
                ('farmer_panchayat', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=50)),
                ('farmer_panchayat', models.CharField(max_length=100)),
                ('farmer_district', models.CharField(max_length=100)),
                ('farmer_phone', models.CharField(max_length=10)),
                ('total_acres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SugarcaneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=50)),
                ('farmer_panchayat', models.CharField(max_length=100)),
                ('farmer_district', models.CharField(max_length=100)),
                ('farmer_phone', models.CharField(max_length=10)),
                ('total_acres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TurmericModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=50)),
                ('farmer_panchayat', models.CharField(max_length=100)),
                ('farmer_district', models.CharField(max_length=100)),
                ('farmer_phone', models.CharField(max_length=10)),
                ('total_acres', models.IntegerField()),
            ],
        ),
    ]
