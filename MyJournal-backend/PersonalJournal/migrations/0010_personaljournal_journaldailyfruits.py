# Generated by Django 4.1.2 on 2022-10-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalJournal', '0009_alter_personaljournal_journalmoodrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaljournal',
            name='JournalDailyFruits',
            field=models.BooleanField(default=False),
        ),
    ]
