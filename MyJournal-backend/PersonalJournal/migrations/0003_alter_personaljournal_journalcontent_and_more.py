# Generated by Django 4.1.2 on 2022-10-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalJournal', '0002_alter_personaljournal_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaljournal',
            name='JournalContent',
            field=models.CharField(default='Journal Post Content', max_length=255),
        ),
        migrations.AlterField(
            model_name='personaljournal',
            name='JournalHeader',
            field=models.CharField(default='Journal Post Title', max_length=255),
        ),
    ]
