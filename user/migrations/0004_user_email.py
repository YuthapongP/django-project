# Generated by Django 4.2.2 on 2023-06-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_rename_food_user_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=60),
        ),
    ]
