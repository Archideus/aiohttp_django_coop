# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='topic',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Topic'),
        ),
    ]
