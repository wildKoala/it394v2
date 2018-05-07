# Generated by Django 2.0.1 on 2018-04-12 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20180302_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('points', models.IntegerField(verbose_name='-')),
                ('assignment_link', models.CharField(default='-', max_length=300)),
                ('objs', models.CharField(default='-', max_length=100)),
                ('date', models.DateField()),
                ('help_resources', models.CharField(default='-', max_length=100)),
                ('lesson_due', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='ClassFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('link', models.CharField(default='', max_length=100)),
            ],
        ),
    ]