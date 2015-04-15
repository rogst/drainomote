# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realserver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ip', models.CharField(max_length=15)),
                ('name', models.CharField(default='Unnamed', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Realserver_Group_Permissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('allow_drain', models.BooleanField(default=True)),
                ('group', models.ForeignKey(to='auth.Group')),
                ('realserver', models.ForeignKey(to='status.Realserver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
