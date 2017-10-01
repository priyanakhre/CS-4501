# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy', models.BooleanField()),
                ('response_limit', models.IntegerField()),
                ('question', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('outcome', models.NullBooleanField()),
                ('min_buyin', models.IntegerField()),
                ('per_person_cap', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('bet_id', models.IntegerField()),
                ('answer', models.BooleanField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('num_tokens', models.IntegerField()),
                ('num_flags', models.IntegerField()),
            ],
        ),
    ]
