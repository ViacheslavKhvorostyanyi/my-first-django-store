# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_productinorder_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]