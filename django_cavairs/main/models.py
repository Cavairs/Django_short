from django.db import models

# Create your models here.


class Phone (models.Model):
    name = models.CharField('Модель телефона', max_length=50)
    image = models.TextField('Изображение телефона')
    price = models.IntegerField('Цена')
    release_date = models.DateField('Дата')
    lte_exists = models.BooleanField('Наличие LTE')
    slug = models.CharField(max_length=50)
