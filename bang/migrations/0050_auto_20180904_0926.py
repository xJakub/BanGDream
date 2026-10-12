# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import magi.utils


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0049_auto_20180829_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='color',
            field=magi.utils.ColorField(max_length=10, null=True, verbose_name='Color', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='i_band',
            field=models.PositiveIntegerField(null=True, verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!')]),
            preserve_default=True,
        ),
    ]
