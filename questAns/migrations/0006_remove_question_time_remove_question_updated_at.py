# Generated by Django 5.1.7 on 2025-03-28 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questAns', '0005_question_time_question_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
    ]
