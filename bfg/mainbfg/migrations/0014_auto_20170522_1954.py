# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-22 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainbfg', '0013_regions_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.SmallIntegerField()),
                ('category_id', models.SmallIntegerField()),
                ('sub_id', models.SmallIntegerField(default=0)),
                ('autor', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=200)),
                ('region_id', models.SmallIntegerField()),
                ('full_adress', models.CharField(blank=True, max_length=350)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('web_site', models.CharField(blank=True, max_length=250)),
                ('is_webstore', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('meta_info', models.CharField(blank=True, max_length=1000)),
                ('main_img', models.ImageField(blank=True, upload_to='images/')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('stop_time', models.DateTimeField(blank=True)),
                ('status', models.SmallIntegerField(default=0)),
                ('type_s', models.SmallIntegerField(default=0)),
                ('type_img_s', models.CharField(max_length=300)),
                ('views', models.IntegerField(default=0)),
                ('phone_views', models.IntegerField(default=0)),
                ('text_message', models.CharField(blank=True, max_length=1000)),
                ('is_paid', models.BooleanField(default=False)),
                ('start_time_paid', models.DateTimeField(blank=True)),
                ('end_time_paid', models.DateTimeField(blank=True)),
                ('on_moderation', models.BooleanField(default=False)),
                ('link_name', models.CharField(max_length=550)),
                ('identifier', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='sentence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainbfg.Sentence'),
        ),
    ]