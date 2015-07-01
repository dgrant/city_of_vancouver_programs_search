# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0002_auto_20150629_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
