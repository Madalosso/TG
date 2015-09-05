# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_algorithms_command'),
    ]

    operations = [
        migrations.RenameField(
            model_name='execution',
            old_name='Algorithm',
            new_name='algorithm',
        ),
        migrations.RemoveField(
            model_name='algorithms',
            name='id',
        ),
        migrations.AddField(
            model_name='algorithms',
            name='idAlg',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
