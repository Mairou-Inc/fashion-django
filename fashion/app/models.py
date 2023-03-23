from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Название")
    sku = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Артикул")
    brand = models.ForeignKey('Brand', null = True, blank=True, default='', on_delete=models.CASCADE, related_name='product' )
    
    class Meta:
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукты'

    def __str__(self):
        return str(self.name)

class Size(models.Model):
    name = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Название")
    product = models.ForeignKey('Product', null = True, blank=True, default='', on_delete=models.CASCADE, related_name='size' )
    class Meta:
        verbose_name = u'Размер'
        verbose_name_plural = u'Размеры'

    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Название")
    class Meta:
        verbose_name = u'Брэнд'
        verbose_name_plural = u'Брэнды'

    def __str__(self):
        return str(self.name)

class Price(models.Model):
    price = models.IntegerField(null = True, blank=True, verbose_name="Цена")
    size = models.ForeignKey('Size', null = True, blank=True, default='', on_delete=models.CASCADE, related_name='price' )
    updatedAt = models.DateTimeField(null = True, blank=True, auto_now=True)
    class Meta:
        verbose_name = u'Цена'
        verbose_name_plural = u'Цены'

    def __str__(self):
        return str(self.price)
