# Generated by Django 5.0.4 on 2024-05-21 17:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Command", "0004_rename_posters_command_poster"),
    ]

    operations = [
        migrations.RenameField(
            model_name="command",
            old_name="poster",
            new_name="posters",
        ),
    ]
