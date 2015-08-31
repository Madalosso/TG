# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariofriends',
            name='date_register',
            field=models.DateField(default=datetime.datetime(2015, 8, 31, 19, 26, 59, 660868, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuariofriends',
            name='last_acess',
            field=models.DateField(default=datetime.datetime(2015, 8, 31, 19, 27, 15, 859482, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
