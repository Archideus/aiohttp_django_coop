# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_remove_channel_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['id'], 'verbose_name': 'Channel', 'verbose_name_plural': 'Channels'},
        ),
        migrations.AlterModelManagers(
            name='channel',
            managers=[
            ],
        ),
    ]
