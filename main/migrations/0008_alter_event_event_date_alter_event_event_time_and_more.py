# Generated by Django 4.0.4 on 2022-04-20 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_orphanage_about_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(1, 0, 27, 730227)),
        ),
        migrations.AlterField(
            model_name='orphanage',
            name='establish_date',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
    ]
