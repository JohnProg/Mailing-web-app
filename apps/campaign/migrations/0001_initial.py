# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('template', '0001_initial'),
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign_name', models.CharField(max_length=60)),
                ('from_name', models.CharField(max_length=120)),
                ('reply_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('subject', models.CharField(max_length=120, null=True, blank=True)),
                ('link_redirect_to', models.URLField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_send', models.DateTimeField(null=True, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'Unpublished'), (1, 'Published')])),
                ('header', models.CharField(max_length=60)),
                ('subtitle', models.CharField(max_length=60)),
                ('body_section1', models.TextField()),
                ('body_section2', models.TextField(null=True, blank=True)),
                ('footer', models.CharField(max_length=60)),
                ('list_contacts', models.ManyToManyField(to='bd.ModuleContactListDB', null=True, blank=True)),
                ('template_campaign', models.OneToOneField(null=True, blank=True, to='template.ModuleTemplate')),
                ('user_list', models.ForeignKey(to='client.Client')),
            ],
        ),
    ]
