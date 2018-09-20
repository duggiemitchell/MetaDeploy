# Generated by Django 2.1.1 on 2018-09-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_slug_changes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planslug',
            old_name='plan',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='productslug',
            old_name='product',
            new_name='parent',
        ),
        migrations.AlterUniqueTogether(
            name='planslug',
            unique_together={('slug', 'parent')},
        ),
    ]