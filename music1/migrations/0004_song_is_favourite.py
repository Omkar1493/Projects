# Generated by Django 2.0.2 on 2018-02-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music1', '0003_remove_song_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
