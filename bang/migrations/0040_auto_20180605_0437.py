# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import magi.utils


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0039_auto_20180520_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='_thumbnail_screenshot',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadThumb('account_screenshot')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='area',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('areas')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='areaitem',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('areas/items')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='_original_english_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('asset/e')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('asset')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='_original_korean_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('asset/k')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='_original_taiwanese_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('asset/t')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_2x_art',
            field=models.ImageField(null=True, upload_to=magi.utils.upload2x('c/art')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_2x_art_trained',
            field=models.ImageField(null=True, upload_to=magi.utils.upload2x('c/art/a')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_2x_transparent',
            field=models.ImageField(null=True, upload_to=magi.utils.upload2x('c/transparent')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_2x_transparent_trained',
            field=models.ImageField(null=True, upload_to=magi.utils.upload2x('c/transparent/a')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_original_art',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('c/art')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_original_art_trained',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('c/art/a')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('c')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_original_image_trained',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('c/a')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_tthumbnail_art',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTthumb('c/art')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_tthumbnail_art_trained',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTthumb('c/art/a')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_tthumbnail_transparent',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTthumb('c/transparent')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='_tthumbnail_transparent_trained',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTthumb('c/transparent/a')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_english_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/e')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_english_rare_stamp',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/stamps/en')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_korean_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/t')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_korean_rare_stamp',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/stamps/kr')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_rare_stamp',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/stamps')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_taiwanese_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/t')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='_original_taiwanese_rare_stamp',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/stamps/tw')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='_thumbnail_screenshot',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadThumb('event_screenshot')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gacha',
            name='_original_english_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/e')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gacha',
            name='_original_korean_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/t')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gacha',
            name='_original_screenshot',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('g')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gacha',
            name='_original_taiwanese_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('e/t')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('items')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('i')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='_original_square_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('i/m')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='playedsong',
            name='_thumbnail_screenshot',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadThumb('song_screenshot')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='_original_image',
            field=models.ImageField(null=True, upload_to=magi.utils.uploadTiny('s')),
            preserve_default=True,
        ),
    ]
