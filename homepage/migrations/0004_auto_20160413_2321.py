# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-13 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_actor_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='E.g. Music', max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='actor',
            name='about',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.SkillCategory'),
        ),
    ]