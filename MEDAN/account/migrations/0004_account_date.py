# Generated by Django 3.2 on 2021-06-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]