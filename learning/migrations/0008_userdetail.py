# Generated by Django 2.2.2 on 2019-06-30 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('learning', '0007_auto_20190630_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
