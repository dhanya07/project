# Generated by Django 2.2.7 on 2020-05-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='educator_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('nphoneno', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('skills', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=20)),
                ('certification', models.CharField(max_length=20)),
                ('charge', models.CharField(max_length=20)),
                ('availabletime', models.CharField(max_length=20)),
                ('image', models.FileField(max_length=20, upload_to='')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
