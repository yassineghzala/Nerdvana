# Generated by Django 5.0.4 on 2024-05-19 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Post", "0003_post_user"),
        ("User", "0003_rename_user_id_user_userid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="dscription",
            new_name="description",
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="User.user"
            ),
        ),
    ]
