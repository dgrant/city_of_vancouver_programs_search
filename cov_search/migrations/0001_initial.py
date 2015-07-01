# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('membership', models.BooleanField()),
                ('description', models.CharField(max_length=200)),
                ('agemin', models.IntegerField()),
                ('agemax', models.IntegerField()),
                ('enrollmin', models.IntegerField()),
                ('enrollmax', models.IntegerField()),
                ('sessions', models.IntegerField()),
                ('numberopen', models.IntegerField()),
                ('numberwaitlisted', models.IntegerField()),
                ('ignoremaximum', models.IntegerField()),
                ('maxenrolledonline', models.IntegerField()),
                ('numberenrolledonline', models.IntegerField()),
                ('dropin', models.BooleanField()),
                ('firstclass', models.BooleanField()),
                ('onlinereg', models.BooleanField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('lac', models.BooleanField()),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('activitytype', models.ForeignKey(to='cov_search.ActivityType')),
                ('agegroup', models.ForeignKey(to='cov_search.AgeGroup')),
                ('category', models.ForeignKey(to='cov_search.Category')),
                ('days', models.ManyToManyField(to='cov_search.Day')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('postalcode', models.CharField(max_length=7)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='program_type',
            field=models.ForeignKey(to='cov_search.ProgramType'),
        ),
        migrations.AddField(
            model_name='program',
            name='season',
            field=models.ForeignKey(to='cov_search.Season'),
        ),
        migrations.AddField(
            model_name='program',
            name='site',
            field=models.ForeignKey(to='cov_search.Site'),
        ),
    ]
