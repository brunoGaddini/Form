# Generated by Django 4.2.1 on 2023-05-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carros",
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
                ("modelo", models.CharField(max_length=150)),
                ("marca", models.CharField(max_length=30)),
                ("ani", models.IntegerField()),
            ],
        ),
    ]
