# Generated by Django 4.0.1 on 2022-01-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_movie_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='booked',
            field=models.BooleanField(default=True),
        ),
    ]
