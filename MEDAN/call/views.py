from django.shortcuts import render
from .models import*
import time

def submit_call(request):
    obj=Call()
    obj.email=request.GET['email']
    obj.name = request.GET['tel']
    obj.name = request.GET['name']
    obj.date=time.strftime('%d.%m.%Y %X')
    obj.save()
    return render(request,'Main/main_page.html')

