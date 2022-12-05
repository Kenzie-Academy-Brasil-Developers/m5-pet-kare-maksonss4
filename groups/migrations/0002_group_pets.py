# Generated by Django 4.1.3 on 2022-12-03 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0002_remove_pet_group"),
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="pets",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group",
                to="pets.pet",
            ),
            preserve_default=False,
        ),
    ]
