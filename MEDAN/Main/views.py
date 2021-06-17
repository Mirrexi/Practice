from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from account.models import Account
from news.models import News
from articles.models import Articles


def main_page(request):
    return render(request, 'main/main_page.html')


def history(request):
    return render(request, 'main/history.html')

def clients(request):
    return render(request, 'main/clients.html')


def map(request):
    return render(request, 'main/map.html')


def newsnews(request):
    new = News.objects.all()
    return render(request, 'main/news-news.html', {'item_list': new})

def newspub(request):
    acc = Account.objects.all()
    return render(request, 'main/news-pub.html',{'item_list':acc})


def sheets(request):
    art = Articles.objects.all()
    return render(request, 'main/sheets.html', {'item_list': art})


def ques(request):
    return render(request, 'main/ques.html')
