# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0003_auto_20150627_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moduletemplate',
            old_name='user_list',
            new_name='owner',
        ),
    ]
