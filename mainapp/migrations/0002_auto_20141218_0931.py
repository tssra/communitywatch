# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='location',
        ),
        migrations.AddField(
            model_name='story',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
            preserve_default=True,
        ),
    ]
