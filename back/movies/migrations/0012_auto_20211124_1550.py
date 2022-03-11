# Generated by Django 3.2.3 on 2021-11-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_remove_movie_trailer_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='youtube_url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]