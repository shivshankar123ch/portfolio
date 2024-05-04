# Generated by Django 5.0.2 on 2024-05-04 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0008_remove_internship_mob_no_internship_phone_no"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="internship",
            name="phone_no",
        ),
        migrations.AddField(
            model_name="internship",
            name="phonenumber",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="portfolio.contact",
            ),
        ),
    ]
