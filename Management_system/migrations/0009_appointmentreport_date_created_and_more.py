# Generated by Django 4.0.3 on 2022-03-23 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Management_system', '0008_appointmentreport_appointmentfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentreport',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='appointmentreport',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_doctor', to=settings.AUTH_USER_MODEL),
        ),
    ]
