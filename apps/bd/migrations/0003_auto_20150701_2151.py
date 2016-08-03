# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0002_auto_20150627_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='name_and_last_name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'Estado', choices=[(0, 'Unpublished'), (1, 'Published')]),
        ),
    ]
