from django.shortcuts import render
from .models import*
import time

def submit_reviews(request):
    obj=Reviews()
    obj.name=request.GET['name']
    obj.email=request.GET['email']
    obj.comment=request.GET['comment']
    obj.date=time.strftime('%d.%m.%Y %X')
    obj.save()
    return render(request,'Main/main_page.html')

