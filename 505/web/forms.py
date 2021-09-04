from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.db.models.base import Model
from django.forms import models
from .models import M_Items, M_Users
from datetime import date
import re
from django.contrib.auth.forms import AuthenticationForm
from hashlib import sha256
import hashlib


class ItemForm(forms.Form):
    item_no = forms.IntegerField(
        label="商品ID：", 
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "form-input", "name": "item_no", })
        )

    item_nm = forms.CharField(
        label='商品名：',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-input", "name": "item_nm",'placeholder':'前方一致'})
        )
        
    register_from = forms.CharField(
        label='開始：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "date", "class": "form-input", "name": "register_from"})
        )
    
    register_to = forms.CharField(
        label='終了：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "date", "class": "form-input", "name": "register_to"})
        )


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = M_Items
        fields = '__all__'
    
    item_no = forms.IntegerField(
        label="商品ID：", 
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "item_no", "readonly": "readonly"})
        )

    item_nm = forms.CharField(
        label='商品名：',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "item_nm"})
        )

    del_flg = forms.CharField(
        label='削除フラグ：', 
        required=False,
        initial=1,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "del_flg", "readonly": "readonly"})
        )
    
    register_dt = forms.CharField(
        label='登録日時：', 
        initial=date.today(),
        widget=forms.TextInput(attrs={"type": "datetime", "class": "input", "name": "register_dt", "readonly": "readonly"})
        )

    version = forms.CharField(
        label='バージョン：', 
        required=False,
        initial=1,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "version", "readonly": "readonly"})
        )
    
    def clean(self):
        return self.cleaned_data


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = M_Items
        fields = '__all__'
    
    item_no = forms.IntegerField(
        label="商品ID：", 
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "item_no", "readonly": "readonly"})
        )

    item_nm = forms.CharField(
        label='商品名：',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "item_nm"})
        )

    del_flg = forms.CharField(
        label='削除フラグ：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "del_flg", "readonly": "readonly"})
        )
    
    register_dt = forms.CharField(
        label='登録日時：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "datetime", "class": "input", "name": "register_dt", "readonly": "readonly"})
        )

    version = forms.CharField(
        label='バージョン：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "version", "readonly": "readonly"})
        )
        
    def clean(self):
        return self.cleaned_data
    
    
class UserForm(forms.Form):
    user_id = forms.IntegerField(
        label="ユーザーID：", 
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "form-input", "name": "user_id"})
        )

    user_name = forms.CharField(
        label='ユーザー名：',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-input", "name": "user_name",'placeholder':'前方一致'})
        )
        
    del_flg = forms.CharField(
        label='削除フラグ：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-input", "name": "del_flg"})
        )


class UserCreateForm(models.ModelForm):
    class Meta:
        model = M_Users
        fields = ('user_id', 'user_name', 'del_flg', 'register_dt', 'version')
    
    user_id = forms.IntegerField(
        label='ユーザーID：',
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "user_id"})
        )

    user_name = forms.CharField(
        label='ユーザー名：',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "item_nm"})
        )
    
    passwd = forms.CharField(
        label='パスワード',
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "passwd",'placeholder':'半角英字と数字を組み合わせて入力'})
        )
    
    del_flg = forms.CharField(
        label='削除フラグ：', 
        required=False,
        initial=0,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "del_flg", "readonly": "readonly"})
        )
    
    register_dt = forms.CharField(
        label='登録日時：', 
        initial=date.today(),
        widget=forms.TextInput(attrs={"type": "datetime", "class": "input", "name": "register_dt", "readonly": "readonly"})
        )

    version = forms.CharField(
        label='バージョン：', 
        required=False,
        initial=1,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "version", "readonly": "readonly"})
        )

    def clean_user_id(self):
        data = self.cleaned_data.get('user_id')
        try:
            user_id = M_Users.objects.get(user_id=data)
            raise forms.ValidationError('登録済みのユーザが存在します。他のユーザIDを入力してください。')
        except M_Users.DoesNotExist:
            return data

    def clean_passwd(self):
        data = self.cleaned_data.get('passwd')
        buf = re.search(r'\A(?=.*?[a-z])(?=.*?\d)[a-z\d]{2,100}\Z(?i)', data)

        if buf is None:
            raise forms.ValidationError('パスワードは半角英字と数字を組み合わせて入力してください。')
        return data
        
    def clean(self):
        return self.cleaned_data
    

class UserUpdateForm(models.ModelForm):
    class Meta:
        model = M_Users
        fields = ('user_id', 'user_name', 'del_flg', 'register_dt', 'version')
    
    user_id = forms.IntegerField(
        label='ユーザーID：',
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "user_id", "readonly": "readonly"})
        )

    user_name = forms.CharField(
        label='ユーザー名：',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "item_nm"})
        )
    
    passwd = forms.CharField(
        label='パスワード',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "passwd",'placeholder':'半角英字と数字を組み合わせて入力'})
        )
    
    del_flg = forms.CharField(
        label='削除フラグ：', 
        required=False,
        initial=0,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "del_flg", "readonly": "readonly"})
        )
    
    register_dt = forms.CharField(
        label='登録日時：', 
        required=False,
        widget=forms.TextInput(attrs={"type": "datetime", "class": "input", "name": "register_dt", "readonly": "readonly"})
        )

    version = forms.CharField(
        label='バージョン：', 
        required=False,
        initial=1,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "version", "readonly": "readonly"})
        )

    def clean_passwd(self):
        data = self.cleaned_data.get('passwd')
        buf = re.search(r'\A(?=.*?[a-z])(?=.*?\d)[a-z\d]{2,100}\Z(?i)', data)
        
        if buf is None:
            raise forms.ValidationError('パスワードは半角英字と数字を組み合わせて入力してください。')
        return data
        
    def clean(self):
        return self.cleaned_data


class LoginForm(forms.Form):
    user_id = forms.IntegerField(
        label='ユーザーID：',
        required=False,
        widget=forms.TextInput(attrs={"type": "number", "class": "input", "name": "user_id"})
        )
    
    passwd = forms.CharField(
        label='パスワード',
        required=False,
        widget=forms.TextInput(attrs={"type": "text", "class": "input", "name": "passwd",'placeholder':'半角英字と数字を組み合わせて入力'})
        )
    
    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data['user_id']
        password = cleaned_data['passwd']

        passwd = hashlib.sha256(password.encode('utf-8')).hexdigest()

        flg = M_Users.objects.filter(user_id=user_id, passwd=passwd, del_flg=0)

        if flg.first() is None:
            raise forms.ValidationError('IDかパスワードに誤りがあります。')
        return self.cleaned_data

    
    
    