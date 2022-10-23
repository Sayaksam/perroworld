# Generated by Django 3.2.8 on 2022-10-21 06:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=2000)),
                ('last_name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=2000)),
                ('number', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=6)),
                ('location', models.CharField(max_length=2000)),
                ('birth_day', models.DateField(null=True)),
                ('follower_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], null=True, size=None)),
                ('post_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], null=True, size=None)),
                ('following_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], null=True, size=None)),
                ('community_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
