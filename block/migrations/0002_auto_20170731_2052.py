# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-31 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': '类别', 'verbose_name_plural': '很多版块'},
        ),
        migrations.AddField(
            model_name='block',
            name='status',
            field=models.IntegerField(choices=[(0, '正常'), (-1, '删除')], default=0, verbose_name='状态'),
            preserve_default=False,
        ),
    ]
