# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulecontactlistdb',
            name='destination',
            field=models.IntegerField(choices=[(1, 'Name'), (2, 'Correo electr\xf3nico')]),
        ),
        migrations.AlterField(
            model_name='modulecontactlistdb',
            name='origin',
            field=models.IntegerField(choices=[(1, 'Name'), (2, 'Correo electr\xf3nico')]),
        ),
    ]
