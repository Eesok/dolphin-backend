from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    category_image = models.TextField()

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100, default='no item name')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    item_image = models.TextField()

    def __str__(self):
        return self.name


class Detail(models.Model):
    measurements = models.CharField(
        max_length=100, default='no detail measurements')
    materials = models.CharField(
        max_length=100, default='no detail materials')
    styles = models.CharField(max_length=100, default='no detail styles')
    brand = models.CharField(max_length=100, default='no detail brand')
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='details')

    def __str__(self):
        return f'{self.measurements}, {self.materials}, {self.styles}, {self.brand}'
