# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0007_auto_20150703_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulecampaign',
            name='body_section1',
            field=models.TextField(null=True, verbose_name=b'Texto del p\xc3\xa1rrafo 1 de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='body_section2',
            field=models.TextField(null=True, verbose_name=b'Texto del p\xc3\xa1rrafo 2 de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='date_send',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de env\xc3\xado', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='subtitle',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Texto del subt\xc3\xadtulo de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='title',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Texto del t\xc3\xadtulo de la plantilla', blank=True),
        ),
    ]
