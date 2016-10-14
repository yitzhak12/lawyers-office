# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers_office', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='email',
            field=models.EmailField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
