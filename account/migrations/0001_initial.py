# Generated by Django 2.2.7 on 2019-12-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('current_price', models.FloatField()),
                ('open_price', models.FloatField()),
                ('previous_close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
    ]
