# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-13 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='parent_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_number',
            field=models.CharField(max_length=10),
        ),
    ]
