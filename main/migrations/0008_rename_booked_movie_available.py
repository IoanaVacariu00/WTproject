# Generated by Django 4.0.1 on 2022-01-09 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_movie_booked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='booked',
            new_name='available',
        ),
    ]
