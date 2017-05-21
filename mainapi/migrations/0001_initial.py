# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-20 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=500)),
                ('Option_A', models.CharField(max_length=200)),
                ('Option_B', models.CharField(max_length=200)),
                ('Option_C', models.CharField(max_length=200)),
                ('Option_D', models.CharField(max_length=200)),
                ('Correct_Option', models.CharField(max_length=200)),
            ],
        ),
    ]
