# Generated by Django 4.0.3 on 2022-03-23 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_available_time_from_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weekdayavailable',
            old_name='email',
            new_name='name',
        ),
    ]
