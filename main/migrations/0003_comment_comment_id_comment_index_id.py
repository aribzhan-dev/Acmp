# Generated by Django 5.1.7 on 2025-03-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tasks_index_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='index_id',
            field=models.IntegerField(default=0),
        ),
    ]
