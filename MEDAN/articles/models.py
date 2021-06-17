from django.db import models

# Create your models here.

class Articles(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.TextField('Заголовок статьи')
    description = models.TextField('Описание статьи')
    content = models.TextField('Статья')
    date = models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f'{self.title} - {self.date}'
