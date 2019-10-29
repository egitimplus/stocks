import itertools

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ad')
    content = models.TextField(verbose_name='Açıklama')
    address = models.TextField(verbose_name='Adres')
    phone = models.CharField(max_length=11, verbose_name='Telefon')
    email = models.EmailField(verbose_name='E-Mail')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yetkili')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    active = models.BooleanField(default=True, verbose_name='Aktif')
    slug = models.CharField(max_length=255, verbose_name='Slug', editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not self.__class__.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)

        super(Company, self).save()