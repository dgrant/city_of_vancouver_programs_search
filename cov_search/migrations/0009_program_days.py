# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0008_remove_program_activitytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='days',
            field=models.ManyToManyField(to='cov_search.Day'),
        ),
    ]
