# Generated by Django 3.2.9 on 2021-11-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='Y37Up2Xnnw', max_length=10),
        ),
    ]
