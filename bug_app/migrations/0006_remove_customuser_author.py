# Generated by Django 3.1.7 on 2021-02-22 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug_app', '0005_customuser_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='author',
        ),
    ]
