# Generated by Django 4.2.5 on 2023-09-22 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Favorite',
        ),
    ]
