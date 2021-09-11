from django.test import TestCase
from django.urls import reverse, resolve
from web.views import IndexView, LoginView, UserView, ItemCreateView, UserCreateView, LogoutView, ItemUpdateView, UserUpdateView
from web.models import M_Items, M_Users
from datetime import date
from django.utils import timezone


class TestUrls(TestCase):
    def test_user_index(self):
        view  = resolve('/index/')
        self.assertEqual(view.func.view_class, IndexView)
    
    def test_item_create(self):
        view  = resolve('/item_create/')
        self.assertEqual(view.func.view_class, ItemCreateView)

    def test_user(self):
        view  = resolve('/user/')
        self.assertEqual(view.func.view_class, UserView)
    
    def test_user_create(self):
        view  = resolve('/user_create/')
        self.assertEqual(view.func.view_class, UserCreateView)

    def test_login(self):
        view  = resolve('/')
        self.assertEqual(view.func.view_class, LoginView)

    def test_logout(self):
        view  = resolve('/logout/')
        self.assertEqual(view.func.view_class, LogoutView)

    def test_item_update(self):
        post = M_Items(item_no='1', item_nm='梨', del_flg=0, register_dt=timezone.localtime() , version=1)
        post.save()
        view = resolve('/item_update/1')
        self.assertEqual(view.func.view_class, ItemUpdateView)
    
    def test_user_update(self):
        post = M_Users(user_id='1', user_name='tanaka', del_flg=0, register_dt=timezone.localtime() , version=1)
        post.save()
        view = resolve('/user_update/1')
        self.assertEqual(view.func.view_class, UserUpdateView)
