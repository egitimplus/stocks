from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools


class ProductManager(models.Manager):
    def active_products(self):
        return self.filter(active=1)


class Product(models.Model):

    items = ProductManager()
    objects = models.Manager()

    name = models.CharField(max_length=100, verbose_name='ürün ismi')
    content = models.TextField(verbose_name='ürün açıklaması', max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(verbose_name='Aktif', default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name='stok_adedi')
    price = models.DecimalField(verbose_name='ürün fiyatı', decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(User, verbose_name='Sahip', on_delete=models.SET_NULL, null=True, blank=True, related_name='products', related_query_name='product')

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/learning/product/detail/%i/' % self.id

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not Product.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)

        super(Product, self).save()

    @property
    def summary(self):
        return self.content[:50]

    @classmethod
    def actives(cls):
        return cls.objects.filter(active=1)

    @staticmethod
    def static_summary(content):
        return content[:50]


class Category(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, related_name='categories', related_query_name='category')

