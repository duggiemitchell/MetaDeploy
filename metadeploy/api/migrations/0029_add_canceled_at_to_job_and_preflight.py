# Generated by Django 2.1.4 on 2018-12-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0028_add_job_preflight_edited_at")]

    operations = [
        migrations.AddField(
            model_name="job", name="canceled_at", field=models.DateTimeField(null=True)
        ),
        migrations.AddField(
            model_name="preflightresult",
            name="canceled_at",
            field=models.DateTimeField(null=True),
        ),
    ]
