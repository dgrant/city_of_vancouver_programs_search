# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0009_program_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='program_type',
            new_name='programtype',
        ),
    ]
