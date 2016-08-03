# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0004_auto_20150627_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='type',
        ),
        migrations.AddField(
            model_name='template',
            name='image_url',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/template/', blank=True),
        ),
    ]
