# Generated by Django 2.2.7 on 2020-05-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educator_tb',
            name='nphoneno',
        ),
        migrations.AddField(
            model_name='educator_tb',
            name='phoneno',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
