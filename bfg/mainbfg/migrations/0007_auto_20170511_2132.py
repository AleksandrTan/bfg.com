# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-11 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbfg', '0006_remove_profile_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='max_num',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='fb_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='vk_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]