# Generated by Django 3.0.8 on 2020-07-29 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20200725_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favori',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='tarih',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 14, 3, 31, 284362, tzinfo=utc)),
        ),
    ]
