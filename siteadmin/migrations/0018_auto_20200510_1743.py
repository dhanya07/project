# Generated by Django 2.2.7 on 2020-05-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0017_user_tb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept_tb',
            name='skillid',
            field=models.ForeignKey(default='1', on_delete='CASCADE', to='siteadmin.skill_tb'),
        ),
    ]
