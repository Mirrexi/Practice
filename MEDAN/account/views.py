from django.shortcuts import render
from .models import *
import time


# Create your views here.
def submit_account(request):
    obj = Account()
    obj.first_name = request.GET['Имя']
    obj.second_name = request.GET['Фамилия']
    obj.position = request.GET['Должность']
    obj.date = time.strftime('%d.%m.%Y %X')
    obj.title = request.GET['Заголовок публикации']
    obj.content = request.GET['Публикация']
    obj.save()
    return render(request, 'Main/main_page.html')
