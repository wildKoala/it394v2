# Generated by Django 2.0.1 on 2018-04-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20180416_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
