# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_add_additional_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedfile',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified date'),
        ),
    ]