# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 15:43
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stacked', '0002_auto_20160519_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymember',
            name='bio',
        ),
        migrations.AddField(
            model_name='familymember',
            name='content',
            field=mezzanine.core.fields.RichTextField(default='', verbose_name='Content'),
            preserve_default=False,
        ),
    ]