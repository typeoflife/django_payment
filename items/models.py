from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    # stripe_product_id = models.CharField(verbose_name='ID товара в базе stripe', max_length=100)
    description = models.TextField(verbose_name='Описание')
    price = models.ForeignKey('Price', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.PositiveIntegerField(verbose_name='Цена')
    stripe_price_id = models.CharField(verbose_name='ID цены товара в базе stripe', max_length=100)
