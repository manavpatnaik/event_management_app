# Generated by Django 3.1.2 on 2020-11-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0009_auto_20201114_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_1.png', null=True, upload_to=''),
        ),
    ]
