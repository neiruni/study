from django.urls import path
from .views import IndexView, ItemCreateView, ItemUpdateView, UserView, UserCreateView, UserUpdateView, LoginView, LogoutView

app_name = 'web'

urlpatterns = [
    path('', LoginView.as_view(),name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('index/', IndexView.as_view(), name='index'),
    path('item_create/', ItemCreateView.as_view(), name='item_create'),
    path('item_update/<int:pk>', ItemUpdateView.as_view(), name='item_update'),
    path('user/', UserView.as_view(), name='user'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
]
