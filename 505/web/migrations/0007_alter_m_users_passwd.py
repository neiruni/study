# Generated by Django 3.2.2 on 2021-08-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210814_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_users',
            name='passwd',
            field=models.CharField(max_length=200),
        ),
    ]