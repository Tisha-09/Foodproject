# Generated by Django 5.1.2 on 2024-11-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('res_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('mobile_number', models.BigIntegerField(unique=True)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
