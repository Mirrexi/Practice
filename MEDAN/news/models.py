from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField('Заголовок новости')
    content = models.TextField('Новость')
    date = models.DateField(auto_now=True, auto_now_add=False)
    img = models.ImageField('Изображение', upload_to='images/')
    def __str__(self):
        return f'{self.title} - {self.date}'
