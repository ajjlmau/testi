# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distro',
            name='kuva',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
