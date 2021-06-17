from django.shortcuts import render
from .models import*

def submit_articles(request):
    obj=Articles()
    obj.title=request.GET['Заголовок статьи']
    obj.description=request.GET['Описании статьи']
    obj.content=request.GET['Статья']
    obj.save()
    return render(request,'Main/main_page.html')

def sheets_articles(request):
    art = Articles.objects.all()
    sheet_id=int(request.GET['sheet_id'])
    sheet=None
    for el in art:
        if el.id==sheet_id:
            sheet=el

    return render(request, 'sheets_articles.html', {'sheet':sheet})