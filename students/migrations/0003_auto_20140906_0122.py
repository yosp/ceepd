# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20140903_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_student',
            field=models.PositiveIntegerField(),
        ),
    ]
