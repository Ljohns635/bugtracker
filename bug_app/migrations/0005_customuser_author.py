# Generated by Django 3.1.7 on 2021-02-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_app', '0004_auto_20210222_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
