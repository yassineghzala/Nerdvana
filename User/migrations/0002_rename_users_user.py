# Generated by Django 5.0.4 on 2024-05-04 17:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Users",
            new_name="User",
        ),
    ]
