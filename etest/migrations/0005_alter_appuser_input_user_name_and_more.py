# Generated by Django 4.2.1 on 2023-05-31 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etest', '0004_appuser_input_user_name_alter_audiodata_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='input_user_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='audiodata',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 31, 14, 27, 11, 600172)),
        ),
    ]
