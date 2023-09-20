# Generated by Django 4.2.3 on 2023-09-20 11:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=40)),
                ("phone", models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name="hostbio",
            name="Hemail",
        ),
        migrations.RemoveField(
            model_name="hostbio",
            name="Hname",
        ),
        migrations.RemoveField(
            model_name="hostbio",
            name="Hphone",
        ),
        migrations.AddField(
            model_name="addcar",
            name="CarSeat",
            field=models.CharField(default="5 Seats", max_length=12),
        ),
        migrations.AddField(
            model_name="car",
            name="isshared",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="car",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.CreateModel(
            name="Trip",
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
                ("cname", models.CharField(max_length=50)),
                ("sdate", models.CharField(max_length=50)),
                ("edate", models.CharField(max_length=50)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trip",
                        to="app.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                ("amount", models.IntegerField()),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car_price",
                        to="app.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Income",
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
                ("cname", models.CharField(max_length=50)),
                ("cinc", models.CharField(max_length=50)),
                ("sidate", models.CharField(max_length=50)),
                ("eidate", models.CharField(max_length=50)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="income",
                        to="app.car",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="app.user"
            ),
            preserve_default=False,
        ),
    ]
