from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='product_name')
    code = models.CharField(max_length=255,
                            verbose_name='product_code')  # по этому полю различаем продукт (код продукта)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    unit = models.CharField(max_length=255, blank=True, null=True)  # единица измерения
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='menu', verbose_name='category')
    # image_url = models.ImageField(upload_to='img_product')  # путь на изображение продукта
    slug = models.SlugField(max_length=150)
    note = models.TextField(blank=True, null=True)  # комментарий к продукту
    class Meta:  # все элементы отображаются по дате создания
        ordering = ['pk']

    def __str__(self):
        return f'name: {self.name}, price: {self.price},  pk: {self.code}'


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='category_name')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='parent_category')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.name
