# Generated by Django 2.2.7 on 2020-05-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0013_accept_tb_skillid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept_tb',
            name='skillid',
            field=models.CharField(default='1', max_length=20),
        ),
    ]