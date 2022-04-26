# Generated by Django 4.0.3 on 2022-03-23 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Management_system', '0007_alter_history_last_checkup'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
                ('reportinfo', models.CharField(blank=True, max_length=50, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management_system.appointment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to='appointment_files')),
                ('appoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management_system.appointmentreport')),
            ],
        ),
    ]
