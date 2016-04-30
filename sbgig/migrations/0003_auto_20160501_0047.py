# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-30 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbgig', '0002_auto_20160425_0130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-datetime']},
        ),
        migrations.AlterIndexTogether(
            name='comment',
            index_together=set([('author', 'datetime'), ('song', 'datetime'), ('gig', 'datetime')]),
        ),
    ]