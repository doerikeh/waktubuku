# Generated by Django 3.0.5 on 2020-06-11 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilebuku', '0003_auto_20200522_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='image_profile',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='slug',
            field=models.ImageField(blank=True, upload_to='image_profile/%Y/%m/%d'),
        ),
    ]