# Generated by Django 3.0 on 2019-12-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='total',
            field=models.FloatField(default=True),
        ),
    ]
