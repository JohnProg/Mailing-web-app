# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20150626_2151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulecampaign',
            options={'verbose_name': 'Campana', 'verbose_name_plural': 'Campanas'},
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='body_section1',
            field=models.TextField(null=True, verbose_name=b'Texto del parrafo 1 de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='body_section2',
            field=models.TextField(null=True, verbose_name=b'Texto del parrafo 2 de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='campaign_name',
            field=models.CharField(max_length=60, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='date_send',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de envio', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='footer',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Texto del pie de pagina de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='from_name',
            field=models.CharField(max_length=120, verbose_name=b'From'),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='header',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Texto en la cabecera de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='link_redirect_to',
            field=models.URLField(null=True, verbose_name=b'Redirigir hacia', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='list_contacts',
            field=models.ManyToManyField(to='bd.ModuleContactListDB', verbose_name=b'Lista de Contactos'),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='reply_email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'Reply', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'Estado', choices=[(0, 'Unpublished'), (1, 'Published')]),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='subject',
            field=models.CharField(max_length=120, null=True, verbose_name=b'Asunto', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='subtitle',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Texto del subtitulo de la plantilla', blank=True),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='template_campaign',
            field=models.OneToOneField(null=True, blank=True, to='template.ModuleTemplate', verbose_name=b'Plantilla'),
        ),
        migrations.AlterField(
            model_name='modulecampaign',
            name='user_list',
            field=models.ForeignKey(verbose_name=b'Cliente', to='client.Client', help_text=b'Seleccionar al cliente o usuario'),
        ),
    ]
