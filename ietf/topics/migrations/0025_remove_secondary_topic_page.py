# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-22 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('bibliography', '0011_bibliographyitem_content_long_title'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0040_page_draft_title'),
        ('topics', '0024_auto_20180205_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primarytosecondaryrelationship',
            name='page',
        ),
        migrations.RemoveField(
            model_name='primarytosecondaryrelationship',
            name='secondary_topic',
        ),
        migrations.RemoveField(
            model_name='secondarypagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='secondarypagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='secondarypagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpage',
            name='area',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpage',
            name='call_to_action',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpage',
            name='mailing_list_signup',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpage',
            name='social_image',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpageperson',
            name='page',
        ),
        migrations.RemoveField(
            model_name='secondarytopicpageperson',
            name='person',
        ),
        migrations.DeleteModel(
            name='PrimaryToSecondaryRelationship',
        ),
        migrations.DeleteModel(
            name='SecondaryPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='SecondaryTopicPage',
        ),
        migrations.DeleteModel(
            name='SecondaryTopicPagePerson',
        ),
    ]
