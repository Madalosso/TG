# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0005_auto_20150905_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithms',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
