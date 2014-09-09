# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_payment', models.PositiveIntegerField()),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('month', models.CharField(max_length=2, choices=[(b'1', b'Enero'), (b'2', b'Febrero'), (b'3', b'Marzo'), (b'4', b'Abril'), (b'5', b'Mayo'), (b'6', b'Junio'), (b'7', b'Julio'), (b'8', b'Agosto'), (b'9', b'Septiembre'), (b'10', b'Octubre'), (b'11', b'Noviembre'), (b'12', b'Diciembre')])),
                ('year_period', models.CharField(max_length=9)),
                ('date_pay', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment_Concept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_payment_concept', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payment',
            name='id_payment_concept',
            field=models.ForeignKey(to='payments.Payment_Concept'),
            preserve_default=True,
        ),
    ]
