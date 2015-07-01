# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0007_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='activitytype',
        ),
    ]
