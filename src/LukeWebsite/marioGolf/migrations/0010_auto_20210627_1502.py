# Generated by Django 3.2.4 on 2021-06-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marioGolf', '0009_delete_tournamentplacement'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hole',
            unique_together={('course', 'holeNumber')},
        ),
        migrations.AlterUniqueTogether(
            name='tournamententry',
            unique_together={('tournament', 'player')},
        ),
        migrations.AlterUniqueTogether(
            name='tournamententryhole',
            unique_together={('tournamentHole', 'tournamentEntry')},
        ),
    ]
