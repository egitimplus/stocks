# Generated by Django 2.2.2 on 2019-06-30 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_auto_20190630_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('page_count', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='learning.Book')),
                ('content', models.TextField()),
            ],
            bases=('learning.book',),
        ),
    ]
