# Generated by Django 2.0.1 on 2018-04-12 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_assignment_classfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='help_resources',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='objs',
        ),
    ]
