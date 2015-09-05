# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0006_algorithms_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithms',
            name='command',
            field=models.CharField(default='Friends', max_length=100),
            preserve_default=False,
        ),
    ]
