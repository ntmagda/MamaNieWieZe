# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160218_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='img',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
