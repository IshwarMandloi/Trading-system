# Generated by Django 3.0 on 2019-12-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_trade_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='total',
            field=models.FloatField(),
        ),
    ]
