from django.db import models
from .company import Company
from django.contrib.auth.models import User


class Dealer(Company):
    staff = models.ManyToManyField(User, related_name='dealers', related_query_name='dealer', blank=True)

    class Meta:
        verbose_name = 'Bayi'
        verbose_name_plural = 'Bayiler'
