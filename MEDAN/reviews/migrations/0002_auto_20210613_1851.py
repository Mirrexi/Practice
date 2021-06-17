# Generated by Django 3.2 on 2021-06-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='comment',
            field=models.TextField(verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.TextField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.TextField(verbose_name='Имя'),
        ),
    ]