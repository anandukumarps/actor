# Generated by Django 4.0.5 on 2022-07-01 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='des',
            new_name='desc',
        ),
    ]
