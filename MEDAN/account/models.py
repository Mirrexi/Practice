from django.db import models
import time

class Account(models.Model):
    first_name = models.TextField('Имя')
    second_name = models.TextField('Фамилия')
    position = models.TextField('Должность')
    date = models.DateField(auto_now=True, auto_now_add=False)
    title= models.TextField('Заголовок публикации')
    content=models.TextField('Публикация')
    def __str__(self):
        return f'{self.title} - {self.date}'
