# Generated by Django 4.2.13 on 2024-10-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель телефона')),
                ('image', models.TextField(verbose_name='Изображение телефона')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('release_date', models.DateField(verbose_name='Дата')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие LTE')),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
    ]
