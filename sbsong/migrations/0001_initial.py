# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 22:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sbgig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Instrument name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'instrument',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggested_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('artist', models.CharField(blank=True, max_length=100, verbose_name='Artist')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('lyrics', models.TextField(blank=True)),
                ('staffed', models.BooleanField(default=False)),
                ('changed_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='last_changed_songs', to=settings.AUTH_USER_MODEL)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='sbgig.Gig')),
                ('suggested_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='suggested_songs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SongLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('notice', models.CharField(blank=True, max_length=150)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='sbsong.Song')),
            ],
        ),
        migrations.CreateModel(
            name='SongPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(blank=True, max_length=200, verbose_name='Notice')),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sbsong.Instrument', verbose_name='Instrument')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='sbsong.Song')),
            ],
        ),
        migrations.CreateModel(
            name='SongPerformer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(blank=True, max_length=200)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbsong.SongPart')),
                ('performer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='songperformer',
            unique_together=set([('part', 'performer')]),
        ),
        migrations.AlterIndexTogether(
            name='song',
            index_together=set([('gig', 'staffed')]),
        ),
    ]
