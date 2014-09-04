# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20140903_2120'),
        ('phones_students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone_student',
            name='student_p',
            field=models.ForeignKey(default='', to='students.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone_student',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
