# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cov_search', '0022_program_fee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agegroup',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='programtype',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['name', 'address']},
        ),
        migrations.AlterField(
            model_name='site',
            name='postalcode',
            field=models.CharField(help_text='', max_length=10),
        ),
    ]
