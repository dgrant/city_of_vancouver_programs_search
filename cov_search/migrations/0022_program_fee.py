# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0021_program_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='fee',
            field=models.DecimalField(default=0, help_text='', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
