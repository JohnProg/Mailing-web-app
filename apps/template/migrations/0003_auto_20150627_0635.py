# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('template', '0002_auto_20150627_0533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moduletemplate',
            options={'verbose_name': 'Modulo Plantilla', 'verbose_name_plural': 'Modulo Plantillas'},
        ),
        migrations.AlterModelOptions(
            name='template',
            options={'verbose_name': 'Plantilla', 'verbose_name_plural': 'Plantillas'},
        ),
        migrations.AddField(
            model_name='moduletemplate',
            name='user_list',
            field=models.ForeignKey(default=1, verbose_name=b'Cliente', to='client.Client', help_text=b'Seleccionar al cliente o usuario'),
            preserve_default=False,
        ),
    ]
