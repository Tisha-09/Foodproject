# Generated by Django 4.1 on 2024-11-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Restaurant", "0005_alter_order_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order", name="del_id", field=models.BigIntegerField(default=0),
        ),
    ]
