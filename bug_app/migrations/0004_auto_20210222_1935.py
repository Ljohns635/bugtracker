# Generated by Django 3.1.7 on 2021-02-22 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug_app', '0003_auto_20210222_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_ticket', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='completed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_ticket', to=settings.AUTH_USER_MODEL),
        ),
    ]
