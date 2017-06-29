# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-27 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mainbfg.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbfg', '0016_auto_20170526_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentensceMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='paid_num',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='image',
            name='sentence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='mainbfg.Sentence'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='dirname_img',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='main_img',
            field=models.ImageField(blank=True, default='nophoto.png', upload_to=mainbfg.models.custom_directory_path),
        ),
    ]
