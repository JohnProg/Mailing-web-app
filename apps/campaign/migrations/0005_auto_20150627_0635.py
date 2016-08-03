# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_auto_20150627_0536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulecampaign',
            options={'verbose_name': 'Modulo Campana', 'verbose_name_plural': 'Modulo Campanas'},
        ),
    ]
