# Generated by Django 4.0.5 on 2022-06-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('des', models.TextField()),
                ('year', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
