from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField('Электронная почта')
    comment = models.TextField('Отзыв')
    date = models.TextField('Дата')

    def __str__(self):
        return f'{self.email} - {self.date}'
