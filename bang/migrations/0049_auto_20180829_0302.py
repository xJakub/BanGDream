# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0048_auto_20180809_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='d_special_bands',
            field=models.TextField(null=True, verbose_name='Band'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='special_band',
            field=models.CharField(max_length=100, null=True, verbose_name='Band'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='areaitem',
            name='i_band',
            field=models.PositiveIntegerField(null=True, verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='i_band',
            field=models.PositiveIntegerField(null=True, verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='i_band',
            field=models.PositiveIntegerField(verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='i_band',
            field=models.PositiveIntegerField(verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!'), (5, 'Glitter*Green'), (6, 'Special Band')]),
            preserve_default=True,
        ),
    ]
