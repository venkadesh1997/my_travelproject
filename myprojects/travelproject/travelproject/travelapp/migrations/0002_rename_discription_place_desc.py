# Generated by Django 3.2.16 on 2022-11-17 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='discription',
            new_name='desc',
        ),
    ]
