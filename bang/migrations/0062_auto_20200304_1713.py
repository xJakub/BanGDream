# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import magi.utils


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0061_auto_20190513_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Start date', validators=[magi.utils.PastOnlyValidator]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='i_band',
            field=models.PositiveIntegerField(help_text="Tagging a band is a shortcut to tagging all the members, so you don't need to tag the members when you tag a band.", null=True, verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!'), (5, 'RAISE A SUILEN'), (6, 'Morfonica')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='i_band',
            field=models.PositiveIntegerField(null=True, verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!'), (5, 'RAISE A SUILEN'), (6, 'Morfonica')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='i_band',
            field=models.PositiveIntegerField(verbose_name='Band', choices=[(0, "Poppin'Party"), (1, 'Afterglow'), (2, 'Pastel*Palettes'), (3, 'Roselia'), (4, 'Hello, Happy World!'), (5, 'RAISE A SUILEN'), (6, 'Morfonica'), (7, 'Glitter*Green'), (8, 'Special Band')]),
            preserve_default=True,
        ),
    ]
