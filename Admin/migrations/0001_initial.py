# Generated by Django 4.1 on 2024-11-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("admin_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=70)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.TextField(max_length=50)),
            ],
        ),
    ]
