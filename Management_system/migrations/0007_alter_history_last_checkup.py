# Generated by Django 4.0.3 on 2022-03-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management_system', '0006_rename_diseae_name_history_disease_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='last_checkup',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]