# Generated by Django 3.0.5 on 2020-05-22 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilebuku', '0002_auto_20200521_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'permissions': (('user', 'Can read user'),)},
        ),
    ]
