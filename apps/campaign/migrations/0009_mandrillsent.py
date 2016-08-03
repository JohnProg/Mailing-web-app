# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0008_auto_20150703_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='MandrillSent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=20)),
                ('_id', models.CharField(max_length=36)),
                ('email', models.EmailField(max_length=254)),
                ('reject_reason', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
