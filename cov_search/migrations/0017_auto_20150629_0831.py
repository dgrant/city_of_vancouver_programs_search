# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0016_auto_20150629_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
