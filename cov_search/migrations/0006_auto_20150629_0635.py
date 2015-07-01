# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0005_auto_20150629_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='days',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
