# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulecampaign',
            name='list_contacts',
            field=models.ManyToManyField(to='bd.ModuleContactListDB'),
        ),
    ]
