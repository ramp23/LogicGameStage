# Generated by Django 2.1.2 on 2018-11-04 23:25

import RoundTable.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoundTable', '0015_auto_20181105_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='RoundTable/default_avatar/default.png', null=True, upload_to=RoundTable.models.User.avatar_upload_to, verbose_name='Аватар'),
        ),
    ]