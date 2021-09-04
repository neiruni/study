# Generated by Django 3.2.2 on 2021-08-14 04:14

import concurrency.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210809_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_items',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=0, help_text='record revision number', verbose_name='バージョン'),
        ),
        migrations.AlterField(
            model_name='m_users',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=0, help_text='record revision number', verbose_name='バージョン'),
        ),
        migrations.AlterField(
            model_name='t_order_details',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=0, help_text='record revision number', verbose_name='バージョン'),
        ),
        migrations.AlterField(
            model_name='t_orders',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=0, help_text='record revision number', verbose_name='バージョン'),
        ),
    ]
