# Generated by Django 4.1.6 on 2023-03-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_profile_quota_mediacloud_legacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='quota_mediacloud_legacy',
            field=models.IntegerField(default=100000),
        ),
    ]
