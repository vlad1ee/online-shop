from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Категория')
    parent = TreeForeignKey('self', verbose_name='Подкатегория',
                            on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = TreeForeignKey(Category, on_delete=models.CASCADE,
                              related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
