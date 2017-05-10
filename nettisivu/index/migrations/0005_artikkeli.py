# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_delete_artikkeli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikkeli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otsikko', models.CharField(max_length=50)),
                ('teksti', models.TextField(max_length=5000)),
                ('kuva', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]