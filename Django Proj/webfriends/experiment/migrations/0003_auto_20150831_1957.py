# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_auto_20150831_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='date_requisition',
            field=models.DateField(auto_now_add=True, verbose_name=b'date_requisition'),
        ),
        migrations.AlterField(
            model_name='usuariofriends',
            name='date_register',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date_register'),
        ),
        migrations.AlterField(
            model_name='usuariofriends',
            name='last_acess',
            field=models.DateTimeField(auto_now=True, verbose_name=b'last_acess'),
        ),
    ]
