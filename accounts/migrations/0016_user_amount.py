# Generated by Django 4.0.3 on 2022-04-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_user_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
