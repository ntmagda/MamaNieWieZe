# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_entry_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/static//img/'),
        ),
    ]