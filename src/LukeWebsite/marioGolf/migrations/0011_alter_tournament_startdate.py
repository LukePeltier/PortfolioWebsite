# Generated by Django 3.2.6 on 2021-08-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marioGolf', '0010_auto_20210627_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
