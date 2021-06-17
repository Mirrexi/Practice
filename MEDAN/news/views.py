from django.shortcuts import render
from .models import*
import time
# Create your views here.
def submit_news(request):
    obj=News()
    obj.title=request.GET['Заголовок новости']
    obj.content = request.GET['Новость']
    obj.img = request.GET['Изображение']
    obj.save()
    return render(request, 'Main/main_page.html')