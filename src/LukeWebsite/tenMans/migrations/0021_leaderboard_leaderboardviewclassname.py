# Generated by Django 3.2.6 on 2021-08-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenMans', '0020_change_charset'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='leaderboardViewClassName',
            field=models.TextField(default=''),
        ),
    ]
