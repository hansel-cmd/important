# Generated by Django 4.2.5 on 2023-09-26 10:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='phone',
            field=models.CharField(default=1234567890, max_length=11, validators=[django.core.validators.MinLengthValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='zipcode',
            field=models.CharField(default=1234567890, max_length=4),
            preserve_default=False,
        ),
    ]
