# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0001_initial'),
        ('students', '0003_auto_20140906_0122'),
        ('courses', '0002_auto_20140906_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_grade_type', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=20, choices=[(b'G', b'General'), (b'C', b'Completivo'), (b'X', b'Extraordinario'), (b'E', b'Especial')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='grades_student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.IntegerField()),
                ('year_period', models.CharField(max_length=9)),
                ('id_course', models.ForeignKey(to='courses.Course')),
                ('id_grade_type', models.ForeignKey(to='grades_student.Grade_Type')),
                ('id_signature', models.ForeignKey(to='signatures.Signature')),
                ('id_student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
