# Generated by Django 4.1.2 on 2022-10-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalJournal', '0008_alter_personaljournal_journalimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaljournal',
            name='JournalMoodRating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]