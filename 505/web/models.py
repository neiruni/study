from django.db import models
from django.db.models.fields import AutoField, CharField
from django.utils import timezone
from concurrency.fields import AutoIncVersionField


class M_Users(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=30)
    passwd = models.CharField(max_length=200)
    del_flg = models.CharField(max_length=1)
    register_dt = models.DateTimeField(default=timezone.now)
    version = AutoIncVersionField(verbose_name='バージョン')

class M_Items(models.Model):
    item_no = models.IntegerField(primary_key=True)
    item_nm = models.CharField(max_length=30)
    del_flg = models.CharField(max_length=1)
    register_dt = models.DateTimeField(default=timezone.now)
    version = AutoIncVersionField(verbose_name='バージョン')


class T_Orders(models.Model):
    user_id = models.CharField(max_length=10)
    order_no = models.IntegerField
    order_data = models.DateField
    shipping_address = models.CharField(max_length=200)
    register_dt = models.DateTimeField(default=timezone.now)
    version = AutoIncVersionField(verbose_name='バージョン')

    unique_together = ['user_id', 'order_no']


class T_Order_Details(models.Model):
    user_id = models.CharField(max_length=10)
    order_no = models.IntegerField
    item_no = models.IntegerField
    quantity = models.IntegerField
    register_dt = models.DateTimeField(default=timezone.now)
    version = AutoIncVersionField(verbose_name='バージョン')

    unique_together = ['user_id', 'order_no', 'item_no']



