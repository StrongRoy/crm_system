# Generated by Django 2.0.7 on 2018-07-15 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='code')),
                ('mobile', models.CharField(max_length=11, verbose_name='mobile')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
            ],
            options={
                'verbose_name': 'SMS code',
                'verbose_name_plural': 'SMS code',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, help_text='Please enter your mobile phone number.', max_length=11, null=True, verbose_name='mobile number'),
        ),
    ]
