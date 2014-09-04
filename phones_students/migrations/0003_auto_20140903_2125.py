# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones_students', '0002_auto_20140903_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone_student',
            old_name='student_p',
            new_name='student_id',
        ),
    ]
