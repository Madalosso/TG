# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_auto_20150831_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='date_requisition',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date_requisition'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
