# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0062_auto_20200304_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-release_date', '-id']},
        ),
        migrations.AlterModelOptions(
            name='collectiblecard',
            options={'ordering': ['-card__i_rarity', '-trained', '-card__release_date']},
        ),
        migrations.AlterModelOptions(
            name='costume',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterModelOptions(
            name='eventparticipation',
            options={'ordering': ['-event__start_date']},
        ),
        migrations.AlterModelOptions(
            name='favoritecard',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='gacha',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='playedsong',
            options={'ordering': ['song__expert_difficulty', 'song_id', '-i_difficulty']},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['-release_date']},
        ),
        migrations.AddField(
            model_name='card',
            name='i_skill_influence',
            field=models.PositiveIntegerField(null=True, verbose_name='{influence}', choices=[(1, 'Power'), (2, 'Cool'), (3, 'Pure'), (4, 'Happy'), (501, "Poppin'Party"), (502, 'Afterglow'), (503, 'Pastel*Palettes'), (504, 'Roselia'), (505, 'Hello, Happy World!'), (506, 'RAISE A SUILEN'), (507, 'Morfonica')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='skill_cond_percentage',
            field=models.FloatField(help_text='0-100', null=True, verbose_name='{cond_percentage}'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='i_skill_special',
            field=models.PositiveIntegerField(null=True, verbose_name='Skill details - Special case', choices=[(0, 'Based off PERFECT notes'), (1, 'Scoreup based on stamina'), (2, 'Better scoreup if you can hit perfects'), (3, 'Based off perfects, but rewards full-band teams'), (4, 'Better scoreup if you can hit perfects, with a band/attribute influence')]),
            preserve_default=True,
        ),
    ]
