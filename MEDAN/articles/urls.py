from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views
urlpatterns = [
    path('sheets_articles', views.sheets_articles, name='sheets_articles'),
    path('submit_articles', views.submit_articles, name = 'submit_articles'),
]