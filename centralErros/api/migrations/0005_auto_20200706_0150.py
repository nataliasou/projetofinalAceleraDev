# Generated by Django 2.2.14 on 2020-07-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200706_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='name',
        ),
        migrations.AddField(
            model_name='log',
            name='title',
            field=models.CharField(default=1, help_text='Enter the error title', max_length=50),
            preserve_default=False,
        ),
    ]
