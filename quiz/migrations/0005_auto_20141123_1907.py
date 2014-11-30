# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20141114_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='title',
            new_name='sex',
        ),
    ]
