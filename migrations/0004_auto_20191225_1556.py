# Generated by Django 3.0.1 on 2019-12-25 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0003_tradder_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tradder',
            old_name='field_name',
            new_name='time',
        ),
    ]
