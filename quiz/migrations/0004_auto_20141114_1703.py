# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='email_id',
            field=models.EmailField(unique=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='title',
            field=models.CharField(max_length=3, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')]),
        ),
    ]
