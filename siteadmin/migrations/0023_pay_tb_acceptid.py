# Generated by Django 2.2.7 on 2020-05-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0022_pay_tb_timid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay_tb',
            name='acceptid',
            field=models.ForeignKey(default='1', on_delete='CASCADE', to='siteadmin.accept_tb'),
        ),
    ]
