# Generated by Django 4.0.3 on 2022-03-23 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management_system', '0004_appointment_appointment_time_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='address',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='hospital_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='sex',
        ),
    ]
