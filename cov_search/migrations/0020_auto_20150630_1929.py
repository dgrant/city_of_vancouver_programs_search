# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0019_auto_20150630_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='programtype',
        ),
        migrations.AddField(
            model_name='category',
            name='programtype',
            field=models.ForeignKey(default=45, to='cov_search.ProgramType', help_text=''),
            preserve_default=False,
        ),
    ]
