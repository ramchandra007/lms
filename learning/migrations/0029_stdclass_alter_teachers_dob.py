# Generated by Django 5.0.1 on 2024-01-11 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0028_delete_topics_alter_teachers_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='stdclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('subid', models.IntegerField()),
                ('chaptername', models.CharField(max_length=100)),
                ('chapterdis', models.TextField(default=None)),
                ('subjecttitle', models.CharField(default=None, max_length=200)),
                ('subject_description', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 11, 9, 51, 15, 704354)),
        ),
    ]
