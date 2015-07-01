# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0018_auto_20150629_1739'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivityType',
        ),
        migrations.AlterField(
            model_name='programtype',
            name='id',
            field=models.IntegerField(help_text='', serialize=False, primary_key=True),
        ),
    ]
