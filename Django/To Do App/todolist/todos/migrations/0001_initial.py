# Generated by Django 4.2.5 on 2023-09-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('updated_at', models.DateTimeField(verbose_name='updated_at')),
            ],
        ),
    ]
