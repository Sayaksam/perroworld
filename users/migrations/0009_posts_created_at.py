# Generated by Django 3.2.8 on 2022-10-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_comments_parentcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
