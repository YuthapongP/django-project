# Generated by Django 5.0.8 on 2024-08-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0009_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=60),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="", max_length=20),
        ),
    ]
