# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0023_auto_20180217_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='side_skill_details',
        ),
        migrations.RemoveField(
            model_name='card',
            name='skill_details',
        ),
        migrations.AddField(
            model_name='card',
            name='i_skill_note_type',
            field=models.PositiveIntegerField(null=True, verbose_name='{note_type}', choices=[(0, 'MISS'), (1, 'BAD'), (2, 'GOOD'), (3, 'GREAT'), (4, 'PERFECT')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='i_skill_special',
            field=models.PositiveIntegerField(null=True, verbose_name='Skill details - Special case', choices=[(0, 'Boost score limited to perfect notes'), (1, 'Boost score based on stamina')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='skill_alt_percentage',
            field=models.FloatField(help_text='0-100', null=True, verbose_name='{alt_percentage}'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='skill_duration',
            field=models.PositiveIntegerField(help_text='in seconds', null=True, verbose_name='{duration}'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='skill_percentage',
            field=models.FloatField(help_text='0-100', null=True, verbose_name='{percentage}'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='skill_stamina',
            field=models.PositiveIntegerField(null=True, verbose_name='{stamina}'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='c_versions',
            field=models.TextField(default='"JP"', null=True, verbose_name='Server availability', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='c_versions',
            field=models.TextField(default='"JP"', null=True, verbose_name='Server availability', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gacha',
            name='c_versions',
            field=models.TextField(default='"JP"', null=True, verbose_name='Server availability', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='c_versions',
            field=models.TextField(default='"JP"', null=True, verbose_name='Server availability', blank=True),
            preserve_default=True,
        ),
    ]
