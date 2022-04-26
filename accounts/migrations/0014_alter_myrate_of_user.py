# Generated by Django 4.0.3 on 2022-03-30 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_myrate_of_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrate',
            name='of_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_rates', to=settings.AUTH_USER_MODEL),
        ),
    ]
