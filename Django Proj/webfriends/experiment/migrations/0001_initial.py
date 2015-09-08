# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithms',
            fields=[
                ('idAlg', models.AutoField(serialize=False, primary_key=True)),
                ('nameAlg', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500, null=True)),
                ('command', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExecModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opt', models.CharField(max_length=100, null=True)),
                ('inputFile', models.FileField(null=True, upload_to=b'')),
                ('desc', models.CharField(max_length=500, null=True)),
                ('algorithm', models.ForeignKey(to='experiment.Algorithms', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_requisition', models.DateTimeField(auto_now_add=True, verbose_name=b'date_requisition')),
                ('status', models.IntegerField(default=1)),
                ('opt', models.CharField(max_length=100, null=True)),
                ('inputFile', models.FileField(null=True, upload_to=b'')),
                ('algorithm', models.ForeignKey(to='experiment.Algorithms', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioFriends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=30, null=True)),
                ('date_register', models.DateTimeField(auto_now_add=True, verbose_name=b'date_register')),
                ('last_acess', models.DateTimeField(auto_now=True, verbose_name=b'last_acess')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='execution',
            name='request_by',
            field=models.ForeignKey(to='experiment.UsuarioFriends'),
        ),
    ]
