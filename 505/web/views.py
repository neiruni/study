from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, View
from .models import M_Items, M_Users
from .forms import ItemCreateForm, ItemForm, ItemUpdateForm, UserForm, UserCreateForm, UserUpdateForm, LoginForm
from .search import SearchView
from django.db.models import Max
from hashlib import sha256
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
import hashlib



class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        params = {
            'form': ItemForm(request.session.get('form_data')),
        }
        return render(request, self.template_name, params)


    def get_context_data(self, **kwargs):
        param = super().get_context_data(**kwargs)
        param['form'] = ItemForm()
        return param

    def post(self, request):
        postlist = request.POST
        object_list = SearchView.fruits_search(postlist)
        params = {
            'object_list': object_list,
            'form': ItemForm(request.POST),
        }
        return render(request, self.template_name, params)


class ItemCreateView(CreateView):
    template_name = 'item_create.html'
    model = M_Items
    form_class = ItemCreateForm

    def post(self, request):
        form = ItemCreateForm(request.POST)

        if not form.is_valid():
            param = {
                'form': ItemCreateForm(request.POST)
            }
            return render(request, 'item_create.html', param)

        latest_item_no = M_Items.objects.all().aggregate(Max('item_no'))
        if latest_item_no['item_no__max'] == None:
            latest_item_no['item_no__max'] = 0

        M_Items.objects.create(
            item_no=latest_item_no['item_no__max'] + 1,
            item_nm=form.cleaned_data['item_nm'],
            del_flg=form.cleaned_data['del_flg'],
            register_dt=form.cleaned_data['register_dt'],
        )

        params = {
            'form': ItemForm(),
        }
        return render(request, 'index.html', params)


class ItemUpdateView(UpdateView):
    template_name = 'item_update.html'
    form_class = ItemUpdateForm
    model = M_Items
    # success_url = reverse_lazy('web:index')

    def post(self, request, pk):
        form = ItemUpdateForm(request.POST)

        if not form.is_valid():
            param = {
                'form': ItemUpdateForm(request.POST)
            }
            return render(request, 'item_update.html', param)

        if 'delete' in request.POST:
            object = M_Items.objects.get(item_no=form.cleaned_data['item_no'])
            post = form.save(commit=False)
            post.item_nm = object.item_nm
            post.del_flg = 0
            post.save()

        elif 'update' in request.POST:
            form.save()

        params = {
                'form': ItemForm(),
            }
        return render(request, 'index.html', params)   


class UserView(TemplateView):
    template_name = 'user.html'

    def get(self, request):
        params = {
            'form': UserForm(request.session.get('form_data')),
        }
        return render(request, self.template_name, params)

    def get_context_data(self, **kwargs):
        param = super().get_context_data(**kwargs)
        param['form'] = UserForm()
        return param
    
    def post(self, request):
        postlist = request.POST
        object_list = SearchView.user_search(postlist)
        params = {
            'object_list': object_list,
            'form': UserForm(request.POST),
        }
        return render(request, self.template_name, params)


class UserCreateView(CreateView):
    template_name = 'user_create.html'
    form_class = UserCreateForm
    model = M_Users

    def post(self, request):
        form = UserCreateForm(request.POST)

        if not form.is_valid():
            param = {
                'form': UserCreateForm(request.POST)
            }
            return render(request, 'user_create.html', param)
        
        data = request.POST["passwd"]
        passwd = hashlib.sha256(data.encode()).hexdigest()
        post = form.save(commit=False)
        post.passwd = passwd
        post.save()

        params = {
            'form': UserForm(),
        }
        return render(request, 'user.html', params)


class UserUpdateView(UpdateView):
    template_name = 'user_update.html'
    form_class = UserUpdateForm
    model = M_Users

    def post(self, request, pk):
        form = UserUpdateForm(request.POST)
        object = M_Users.objects.get(user_id=request.POST['user_id'])

        if 'delete' in request.POST:
            object.del_flg = 1
            object.save()
            
            params = {
                'form': UserForm(),
            }
            return render(request, 'user.html', params)   
     
        if not form.is_valid():
            param = {
                'form': UserUpdateForm(request.POST)
            }
            return render(request, 'user_update.html', param)

        if 'update' in request.POST:
            if form.cleaned_data['user_id'] == '':
                post = form.save(commit=False)
                post.passwd = object.passwd 
                post.save()
            else:
                data = request.POST["passwd"]
                passwd = hashlib.sha256(data.encode()).hexdigest()
                post = form.save(commit=False)
                post.passwd = passwd
                post.save()

        params = {
                'form': UserForm(),
            }
        return render(request, 'user.html', params)   
 

class LoginView(View):
    def get(self, request):
        params = {
                'form': LoginForm(),
            }
        return render(request, 'login.html', params) 

    def post(self, request):
        form = LoginForm(request.POST)

        if not form.is_valid():
            params = {
                'form': LoginForm(request.POST)
            }
            return render(request, 'login.html', params)
        
        params = {
                'form': ItemForm(),
            }
        return render(request, 'index.html', params)


class LogoutView(LogoutView):
    template_name = 'logout.html'



