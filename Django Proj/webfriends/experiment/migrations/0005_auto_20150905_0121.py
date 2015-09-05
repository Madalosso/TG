# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0004_auto_20150904_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameAlg', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='execution',
            name='opt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='execution',
            name='Algorithm',
            field=models.ForeignKey(to='experiment.Algorithms', null=True),
        ),
    ]
