# Generated by Django 3.1.3 on 2021-06-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210613_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]