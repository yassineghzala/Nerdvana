# Generated by Django 5.0.4 on 2024-05-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Post", "0006_rename_user_post_userid_post_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="imageURL",
            field=models.FileField(upload_to="images/"),
        ),
    ]
