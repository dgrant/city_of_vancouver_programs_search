# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0012_auto_20150629_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='program',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='program',
            name='startdate',
        ),
        migrations.RemoveField(
            model_name='program',
            name='starttime',
        ),
    ]
