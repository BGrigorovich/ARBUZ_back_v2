# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Crimes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('year_month', models.DateField(max_length=8)),
                ('total', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
                ('bodily_harm_with_fatal_cons', models.IntegerField(default=0)),
                ('brigandage', models.IntegerField(default=0)),
                ('drugs', models.IntegerField(default=0)),
                ('extortion', models.IntegerField(default=0)),
                ('fraud', models.IntegerField(default=0)),
                ('grave_and_very_grave', models.IntegerField(default=0)),
                ('hooliganism', models.IntegerField(default=0)),
                ('intentional_injury', models.IntegerField(default=0)),
                ('looting', models.IntegerField(default=0)),
                ('murder', models.IntegerField(default=0)),
                ('rape', models.IntegerField(default=0)),
                ('theft', models.IntegerField(default=0)),
                ('building_id', models.ForeignKey(to='core.Building', related_name='crimes')),
            ],
        ),
    ]
