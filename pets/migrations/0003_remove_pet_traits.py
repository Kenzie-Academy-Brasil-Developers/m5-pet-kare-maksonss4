# Generated by Django 4.1.3 on 2022-12-05 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0002_remove_pet_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="traits",
        ),
    ]
