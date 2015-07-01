# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0017_auto_20150629_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agegroup',
            name='name',
            field=models.CharField(help_text='', unique=True, max_length=10, db_index=True),
        ),
        migrations.AlterField(
            model_name='programtype',
            name='name',
            field=models.CharField(help_text='', unique=True, max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(help_text='', unique=True, max_length=50, db_index=True),
        ),
    ]
