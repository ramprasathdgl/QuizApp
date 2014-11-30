# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20141123_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultPercentage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Percentage', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
