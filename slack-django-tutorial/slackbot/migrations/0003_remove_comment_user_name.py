# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-03 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slackbot', '0002_auto_20171203_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
    ]
