# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import experiment.models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execmodel',
            name='inputFile',
            field=models.FileField(null=True, upload_to=b'presetsInputs/'),
        ),
        migrations.AlterField(
            model_name='execution',
            name='inputFile',
            field=models.FileField(null=True, upload_to=experiment.models.user_directory_path),
        ),
    ]
