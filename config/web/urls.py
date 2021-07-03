from os import name
from django.urls import path
from django.views.generic.list import ListView
from .views import FruitsListView, IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('list/', FruitsListView.as_view(), name='list'),
]
