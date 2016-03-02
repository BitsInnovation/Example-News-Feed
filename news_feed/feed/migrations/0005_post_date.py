# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20160302_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 16, 41, 12, 259308, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
