# Generated by Django 2.1.2 on 2018-11-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0016_use_hashids")]

    operations = [
        migrations.AddField(
            model_name="job",
            name="status",
            field=models.CharField(
                choices=[
                    ("started", "started"),
                    ("complete", "complete"),
                    ("failed", "failed"),
                ],
                default="started",
                max_length=64,
            ),
        )
    ]
