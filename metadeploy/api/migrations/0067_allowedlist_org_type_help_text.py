# Generated by Django 2.2 on 2019-04-15 13:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0066_remove_blank_choice_from_allowedlist")]

    operations = [
        migrations.AlterField(
            model_name="allowedlist",
            name="org_type",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("Production", "Production"),
                        ("Scratch", "Scratch"),
                        ("Sandbox", "Sandbox"),
                        ("Developer", "Developer"),
                    ],
                    max_length=64,
                ),
                default=list,
                help_text="All orgs of these types will be automatically allowed.",
                size=4,
            ),
        )
    ]
