# Generated by Django 5.0.8 on 2024-08-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=60, unique=True),
        ),
    ]
