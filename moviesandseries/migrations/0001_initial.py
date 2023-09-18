# Generated by Django 4.2.5 on 2023-09-15 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('film_director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=50)),
                ('kind_of_movies', models.CharField(max_length=100)),
                ('qualification', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('release_year', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('film_director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=50)),
                ('kind_of_series', models.CharField(max_length=100)),
                ('qualification', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('release_year', models.DateTimeField()),
                ('seasons', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('episode', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
            ],
        ),
    ]
