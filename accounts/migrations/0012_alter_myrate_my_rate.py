# Generated by Django 4.0.3 on 2022-03-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_myrate_of_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrate',
            name='my_rate',
            field=models.IntegerField(null=True),
        ),
    ]
