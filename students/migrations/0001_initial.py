# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_student', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('birthday', models.DateField()),
                ('photo', models.ImageField(upload_to=b'students')),
                ('sex', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
