# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_course', models.IntegerField()),
                ('section', models.CharField(max_length=1, choices=[(b'A', b'Diurno'), (b'B', b'Tarde'), (b'N', b'N/A')])),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('amount', models.DecimalField(max_digits=18, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
