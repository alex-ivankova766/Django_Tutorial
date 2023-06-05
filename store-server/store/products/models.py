from django.db import models

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity= models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f'Продукт: {self.product_name} | Категория: {self.category}'


