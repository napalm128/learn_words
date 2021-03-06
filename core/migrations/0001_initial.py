# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 16:25
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=1)),
                ('word', models.CharField(max_length=255, null=True)),
                ('translation', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('part_of_speach', models.CharField(max_length=255, null=True)),
                ('frequency', models.IntegerField()),
                ('dispersion', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WordScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answers_in_a_row', models.IntegerField(default=0)),
                ('times_appeared', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Word')),
            ],
        ),
    ]
