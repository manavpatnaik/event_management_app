# Generated by Django 3.1.2 on 2020-11-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0007_auto_20201113_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
