# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='topping',
            new_name='text',
        ),
    ]