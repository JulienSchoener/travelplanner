# Generated by Django 4.2.4 on 2023-09-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0002_hotelbooking_meeting"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessPartner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=15)),
            ],
        ),
    ]