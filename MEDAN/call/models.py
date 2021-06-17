from django.db import models


class Call(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField('Электронная почта')
    phone = models.CharField(max_length=12)
    date = models.TextField('Дата')

    def __str__(self):
        return f'{self.email} - {self.date}'
