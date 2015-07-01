# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0010_auto_20150629_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agegroup',
            name='name',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
