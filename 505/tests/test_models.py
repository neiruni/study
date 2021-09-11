from django.test import TestCase
from web.models import M_Users, M_Items, T_Orders, T_Order_Details
from datetime import date
from django.utils import timezone


class M_ItemsModelTests(TestCase):
    def test_is_empty(self):
        saves_post = M_Items.objects.all()
        self.assertEqual(saves_post.count(), 0)
    
    def test_is_count_one(self):
        post = M_Items(item_no='1', item_nm='梨', del_flg=0, register_dt=timezone.localtime() , version=1)
        post.save()
        save_posts = M_Items.objects.all()
        self.assertEqual(save_posts.count(), 1)

