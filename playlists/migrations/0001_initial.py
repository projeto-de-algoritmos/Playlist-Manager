# Generated by Django 3.2.7 on 2021-09-26 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('popularity', models.PositiveSmallIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('artists', models.CharField(max_length=200)),
                ('album_name', models.CharField(max_length=200)),
                ('album_image', models.CharField(max_length=200)),
                ('playlists', models.ManyToManyField(to='playlists.Playlist')),
            ],
        ),
    ]
