# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20141126_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultpercentage',
            name='fifthquarter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
