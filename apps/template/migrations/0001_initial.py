# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(max_length=60, verbose_name='Template name')),
                ('colors', models.TextField(null=True, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'Unpublished'), (1, 'Published')])),
                ('cover_image', models.CharField(max_length=250, null=True, blank=True)),
                ('base64_url', models.TextField(null=True, blank=True)),
                ('selected', models.IntegerField(default=0, choices=[(0, 'Not Selected'), (1, 'Selected')])),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=b'/template/')),
                ('status', models.IntegerField(default=0, choices=[(0, 'Unpublished'), (1, 'Published')])),
                ('created_add', models.DateTimeField(auto_now_add=True)),
                ('updated_add', models.DateTimeField(auto_now=True)),
                ('type', models.IntegerField(default=0, verbose_name='Template type', choices=[(0, 'Mailing Template'), (1, 'Module Template')])),
            ],
        ),
        migrations.AddField(
            model_name='moduletemplate',
            name='module_template',
            field=models.ForeignKey(blank=True, to='template.Template', null=True),
        ),
    ]
