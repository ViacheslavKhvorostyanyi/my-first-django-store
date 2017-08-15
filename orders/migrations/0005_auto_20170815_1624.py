# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_productinorder_prise'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_prise',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_prise',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
