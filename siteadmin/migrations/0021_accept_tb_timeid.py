# Generated by Django 2.2.7 on 2020-05-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0020_accept_tb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='accept_tb',
            name='timeid',
            field=models.ForeignKey(default='1', on_delete='CASCADE', to='siteadmin.time_tb'),
        ),
    ]