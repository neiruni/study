from django.urls import path
from .views import FruitsListView, IndexView, FruitsView,  FruitsCreateView, FruitsDetailView

app_name = 'web'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    # path('list/', FruitsListView.as_view(), name='list'),
    path('fruits/', FruitsView.as_view(), name='fruits'),
    path('fruits/new', FruitsCreateView.as_view(), name='fruitscreate'),
    path('fruits/<int:id>', FruitsDetailView.as_view(), name='fruitsdetail'),
]
