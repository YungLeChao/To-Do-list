# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0005_auto_20160320_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='shared_lists'),
            preserve_default=True,
        ),
    ]
