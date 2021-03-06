# Generated by Django 4.0.3 on 2022-03-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management_system', '0009_appointmentreport_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Waiting for receiver', 'Waiting for receiver'), ('Delivered', 'Delivered')], default='Pending', max_length=100, null=True),
        ),
    ]
