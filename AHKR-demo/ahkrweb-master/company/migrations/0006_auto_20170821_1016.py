# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20170818_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignproduct',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_product', to='product.Product', verbose_name='Product'),
        ),
    ]
