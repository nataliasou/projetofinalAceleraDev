# Generated by Django 2.2.14 on 2020-07-05 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorinstances',
            name='events',
            field=models.IntegerField(help_text='Enter the error code'),
        ),
    ]