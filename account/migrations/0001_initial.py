# Generated by Django 3.1.1 on 2020-10-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoulmetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_introduction', models.TextField(max_length=140, verbose_name='自己紹介')),
                ('area', models.CharField(max_length=50, verbose_name='地域')),
                ('plan', models.TextField(max_length=50, null=True, verbose_name='プラン')),
                ('base_price', models.IntegerField(verbose_name='基本料金')),
                ('is_pass', models.BooleanField(null=True, verbose_name='審査合格フラグ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
        migrations.CreateModel(
            name='OptionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100, verbose_name='オプション内容')),
                ('price', models.IntegerField(verbose_name='追加料金')),
            ],
        ),
    ]
