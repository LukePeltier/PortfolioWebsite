# Generated by Django 3.2.4 on 2021-06-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marioGolf', '0006_alter_tournamentplacement_tournamententry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hole',
            name='distanceFromTee',
        ),
    ]
