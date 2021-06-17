from django.urls import path,include
from . import views
#from django.conf.urls import include, url


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('history', views.history, name='history'),
    path('map', views.map, name='map'),
    path('news-news', views.newsnews, name='news-news'),
    path('news-pub', views.newspub, name='news-pub'),
    path('sheets/', views.sheets, name='sheets'),
    path('ques', views.ques, name='ques'),
    path('clients', views.clients, name='clients'),
    path('articles/', include('articles.urls')),
]
