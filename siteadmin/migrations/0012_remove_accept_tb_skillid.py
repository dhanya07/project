# Generated by Django 2.2.7 on 2020-05-10 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0011_accept_tb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accept_tb',
            name='skillid',
        ),
    ]