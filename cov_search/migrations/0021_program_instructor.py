# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0020_auto_20150630_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='instructor',
            field=models.ForeignKey(to='cov_search.Instructor', help_text='', null=True),
        ),
    ]
