# Generated by Django 3.1.1 on 2020-10-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201001_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goulmetmodel',
            name='opiton',
        ),
    ]
