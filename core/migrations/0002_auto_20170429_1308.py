# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 13:08
from __future__ import unicode_literals

import json

from django.db import migrations, models


def order_words_by_labuage(apps, schema_editor):
    Word = apps.get_model("core", "Word")
    for word in Word.objects.all():
        word.word_en = word.word_en
        word.word_ru = ';'.join(word.translation.get('ru', ''))
        word.word_uk = ';'.join(word.translation.get('ua', ''))
        word.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='word',
            new_name='word_en',
        ),
        migrations.AddField(
            model_name='word',
            name='word_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='word_uk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RunPython(order_words_by_labuage),
        migrations.RemoveField(
            model_name='word',
            name='translation',
        ),
    ]
