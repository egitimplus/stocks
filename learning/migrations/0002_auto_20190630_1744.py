# Generated by Django 2.2.2 on 2019-06-30 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sahip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Aktif'),
        ),
    ]
