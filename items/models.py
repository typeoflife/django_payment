from django.db import models

class Item(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')