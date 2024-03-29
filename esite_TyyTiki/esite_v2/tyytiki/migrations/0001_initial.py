# Generated by Django 5.0.1 on 2024-02-21 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('posted', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tyytiki.category')),
            ],
            options={
                'verbose_name': 'Изделие',
                'verbose_name_plural': 'Изделия',
            },
        ),
    ]
