# Generated by Django 2.1.2 on 2018-10-26 13:03

import RoundTable.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoundTable', '0010_auto_20181026_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='teams',
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='RoundTable/default_avatar/default.png', upload_to=RoundTable.models.User.avatar_upload_to, verbose_name='Аватар'),
        ),
    ]
