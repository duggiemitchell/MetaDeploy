# Generated by Django 2.1.1 on 2018-09-07 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_add_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
            ),
            preserve_default=False,
        ),
    ]