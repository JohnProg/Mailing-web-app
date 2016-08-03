# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleContactListDB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_name', models.CharField(max_length=120, verbose_name='Title')),
                ('origin', models.IntegerField(choices=[(1, 'Nombre'), (2, 'Correo electr\xf3nico')])),
                ('destination', models.IntegerField(choices=[(1, 'Nombre'), (2, 'Correo electr\xf3nico')])),
                ('status', models.IntegerField(default=0, choices=[(0, 'Unpublished'), (1, 'Published')])),
                ('created_add', models.DateTimeField(auto_now_add=True)),
                ('updated_add', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='client.Client')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='list_owner',
            field=models.ForeignKey(to='bd.ModuleContactListDB'),
        ),
    ]
