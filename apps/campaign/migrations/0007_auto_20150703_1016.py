# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0006_auto_20150627_0638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modulecampaign',
            old_name='header',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='modulecampaign',
            name='footer',
        ),
    ]
