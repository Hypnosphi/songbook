# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sb', '0012_songpart_required'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='songwatcher',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='songwatcher',
            name='song',
        ),
        migrations.RemoveField(
            model_name='songwatcher',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='userplays',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='userplays',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='userplays',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='songlink',
            unique_together=set([]),
        ),
        migrations.DeleteModel(
            name='SongWatcher',
        ),
        migrations.DeleteModel(
            name='UserPlays',
        ),
    ]
