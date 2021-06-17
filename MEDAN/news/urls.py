from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views
urlpatterns = [
    path('', include(('Main.urls', 'Main'), namespace='Main')),
    path('submit_news', views.submit_news, name = 'submit_news'),
]