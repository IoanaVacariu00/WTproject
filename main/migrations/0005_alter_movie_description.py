# Generated by Django 4.0.1 on 2022-01-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
