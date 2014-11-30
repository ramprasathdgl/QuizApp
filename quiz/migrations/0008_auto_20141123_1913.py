# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20141123_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='sex',
            field=models.CharField(max_length=10, choices=[(b'MR', b'Male'), (b'MRS', b'Female'), (b'MS', b'Other')]),
        ),
    ]
