# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sb', '0011_auto_20160423_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='songpart',
            name='required',
            field=models.BooleanField(default=True),
        ),
    ]