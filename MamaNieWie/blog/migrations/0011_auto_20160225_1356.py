# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160218_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/media/'),
        ),
    ]