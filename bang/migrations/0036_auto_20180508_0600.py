# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0035_auto_20180504_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='i_band',
            field=models.PositiveIntegerField(verbose_name='Band', choices=[(0, "Poppin' Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!')]),
            preserve_default=True,
        ),
    ]
