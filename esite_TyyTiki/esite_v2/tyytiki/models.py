from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Product(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание изделия')
    price = models.IntegerField(default=0, verbose_name='Цена')
    posted = models.BooleanField(default=True, verbose_name='Добавлено')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_id': self.pk})

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'
