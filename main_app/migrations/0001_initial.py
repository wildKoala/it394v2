# Generated by Django 2.0.1 on 2018-03-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('title', models.CharField(default='', max_length=100)),
                ('reading', models.CharField(default='', max_length=100)),
                ('notes', models.CharField(default='', max_length=300)),
                ('assigns_due', models.CharField(default='', max_length=100)),
                ('objs', models.CharField(default='', max_length=100)),
                ('date', models.DateField()),
                ('help_resources', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
