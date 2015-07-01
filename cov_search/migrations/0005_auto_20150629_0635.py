# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0004_auto_20150629_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programtype',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
