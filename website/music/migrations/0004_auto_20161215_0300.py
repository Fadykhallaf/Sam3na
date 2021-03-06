# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20161213_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=250),
        ),
    ]
