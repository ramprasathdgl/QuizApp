# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_resultpercentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultpercentage',
            name='Percentage',
        ),
        migrations.AddField(
            model_name='resultpercentage',
            name='firstquarter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultpercentage',
            name='fourthquarter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultpercentage',
            name='secondquarter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultpercentage',
            name='thirdquarter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
