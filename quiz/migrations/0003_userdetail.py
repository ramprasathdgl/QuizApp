# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20141109_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title          :', max_length=3, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')])),
                ('name', models.CharField(help_text=b'Name          :', max_length=100)),
                ('email_id', models.EmailField(help_text=b'Email-Id      :', max_length=70)),
                ('birth_date', models.DateField(help_text=b'DateOfBirth    :', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
