# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0005_auto_20150701_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='image_url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
