# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0005_auto_20150627_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modulecampaign',
            old_name='user_list',
            new_name='owner',
        ),
    ]
