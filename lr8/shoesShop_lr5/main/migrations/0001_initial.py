# Generated by Django 3.1.4 on 2020-12-21 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Цвет',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Производитель',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.IntegerField(verbose_name='Артикул')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
                ('size', models.CharField(max_length=10, verbose_name='Размер')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category', verbose_name='Категория')),
                ('color', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.color', verbose_name='Цвет')),
                ('manufacturer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.manufacturer', verbose_name='Производитель')),
            ],
        ),
    ]
