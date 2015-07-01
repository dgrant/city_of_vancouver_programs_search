# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0014_auto_20150629_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
