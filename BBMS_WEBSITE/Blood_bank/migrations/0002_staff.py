# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=10)),
            ],
        ),
    ]