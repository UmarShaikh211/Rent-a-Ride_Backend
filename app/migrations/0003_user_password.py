# Generated by Django 4.2.3 on 2023-09-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
