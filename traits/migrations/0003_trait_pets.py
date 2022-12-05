# Generated by Django 4.1.3 on 2022-12-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0003_remove_pet_traits"),
        ("traits", "0002_trait_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="pets",
            field=models.ManyToManyField(related_name="traits", to="pets.pet"),
        ),
    ]
