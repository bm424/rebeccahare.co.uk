# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_actor_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='about',
            field=models.TextField(default=''),
        ),
    ]