# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_auto_20150627_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulecampaign',
            name='template_campaign',
            field=models.ForeignKey(default=1, verbose_name=b'Plantilla', to='template.ModuleTemplate'),
            preserve_default=False,
        ),
    ]
