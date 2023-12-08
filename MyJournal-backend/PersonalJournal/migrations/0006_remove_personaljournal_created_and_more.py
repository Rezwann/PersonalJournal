# Generated by Django 4.1.2 on 2022-10-21 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalJournal', '0005_remove_personaljournal_modified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaljournal',
            name='Created',
        ),
        migrations.AddField(
            model_name='personaljournal',
            name='JournalImage',
            field=models.ImageField(default='static/Nature.svg', upload_to='static/'),
        ),
        migrations.AddField(
            model_name='personaljournal',
            name='LastModified',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 21, 20, 40, 15, 46153, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personaljournal',
            name='JournalContent',
            field=models.TextField(default='Journal Post Content', max_length=255),
        ),
    ]