from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
import datetime
from django.views.generic.base import View
from .data import FruitsData, ArticleSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FruitsForm


class IndexView(TemplateView):
    template_name = 'index.html'

    #日時、曜日を返す
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        day = datetime.date.today()
        context["dt"] = str(day.strftime("%Y/%m/%d")) + ' ' + str(day.strftime('%A'))
        return context
        

class FruitsListView(TemplateView):
    template_name = 'fruits.html'

    def get(self, request):
        #リスト作成
        fruitslist = [
            ['1', 'めろん', '高いよ',], ['2', 'りんご', 'おいしいよ'], ['3', 'マスカット', 'つぶつぶです'],
            ['4', 'めろん', '高いよ',], ['5', 'りんご', 'おいしいよ'], ['6', 'マスカット', 'つぶつぶです'],
            ['7', 'めろん', '高いよ',], ['8', 'りんご', 'おいしいよ'], ['9', 'マスカット', 'つぶつぶです'],
            ['10', 'めろん', '高いよ',], ['11', 'りんご', 'おいしいよ'], ['12', 'マスカット', 'つぶつぶです'],
            ['13', 'めろん', '高いよ',], ['14', 'りんご', 'おいしいよ'], ['15', 'マスカット', 'つぶつぶです'],
            ['16', 'めろん', '高いよ',], ['17', 'りんご', 'おいしいよ'], ['18', 'マスカット', 'つぶつぶです'],
            ['19', 'めろん', '高いよ',], ['20', 'りんご', 'おいしいよ'], ['21', 'マスカット', 'つぶつぶです'],
            ['22', 'めろん', '高いよ',], ['23', 'りんご', 'おいしいよ'], ['24', 'マスカット', 'つぶつぶです'],
            ['25', 'めろん', '高いよ',], ['26', 'りんご', 'おいしいよ'], ['27', 'マスカット', 'つぶつぶです'],
            ['28', 'めろん', '高いよ',], ['29', 'りんご', 'おいしいよ'], ['30', 'マスカット', 'つぶつぶです'],
            ['31', 'めろん', '高いよ',], ['32', 'りんご', 'おいしいよ'], ['33', 'マスカット', 'つぶつぶです'], 
            ['34', 'めろん', '高いよ',], ['35', 'りんご', 'おいしいよ'], ['36', 'マスカット', 'つぶつぶです'],
            ['37', 'めろん', '高いよ',], ['38', 'りんご', 'おいしいよ'], ['39', 'マスカット', 'つぶつぶです'],
            ['40', 'めろん', '高いよ',], ['41', 'りんご', 'おいしいよ'], ['42', 'マスカット', 'つぶつぶです'],
            ['43', 'めろん', '高いよ',], ['44', 'りんご', 'おいしいよ'], ['45', 'マスカット', 'つぶつぶです'],
            ['46', 'めろん', '高いよ',], ['47', 'りんご', 'おいしいよ'], ['48', 'マスカット', 'つぶつぶです'],
            ['49', 'めろん', '高いよ',], ['50', 'りんご', 'おいしいよ'], ['51', 'マスカット', 'つぶつぶです'],
            ['52', 'めろん', '高いよ',], ['53', 'りんご', 'おいしいよ'], ['54', 'マスカット', 'つぶつぶです'],
            ['55', 'めろん', '高いよ',], ['56', 'りんご', 'おいしいよ'], ['57', 'マスカット', 'つぶつぶです'],
            ['58', 'めろん', '高いよ',], ['59', 'りんご', 'おいしいよ'], ['60', 'マスカット', 'つぶつぶです'],
            ['61', 'めろん', '高いよ',], ['62', 'りんご', 'おいしいよ'], ['63', 'マスカット', 'つぶつぶです'],
            ['64', 'めろん', '高いよ',], ['65', 'りんご', 'おいしいよ'], ['66', 'マスカット', 'つぶつぶです'], 
            ['67', 'めろん', '高いよ',], ['68', 'りんご', 'おいしいよ'], ['69', 'マスカット', 'つぶつぶです'],
            ['70', 'めろん', '高いよ',], ['71', 'りんご', 'おいしいよ'], ['72', 'マスカット', 'つぶつぶです'],
            ['73', 'めろん', '高いよ',], ['74', 'りんご', 'おいしいよ'], ['75', 'マスカット', 'つぶつぶです'],
            ['76', 'めろん', '高いよ',], ['77', 'りんご', 'おいしいよ'], ['78', 'マスカット', 'つぶつぶです'],
            ['79', 'めろん', '高いよ',], ['80', 'りんご', 'おいしいよ'], ['81', 'マスカット', 'つぶつぶです'],
            ['82', 'めろん', '高いよ',], ['83', 'りんご', 'おいしいよ'], ['84', 'マスカット', 'つぶつぶです'], 
            ['85', 'めろん', '高いよ',], ['86', 'りんご', 'おいしいよ'], ['87', 'マスカット', 'つぶつぶです'],
            ['88', 'めろん', '高いよ',], ['89', 'りんご', 'おいしいよ'], ['90', 'マスカット', 'つぶつぶです'],
            ['91', 'めろん', '高いよ',], ['92', 'りんご', 'おいしいよ'], ['93', 'マスカット', 'つぶつぶです'],
            ['94', 'めろん', '高いよ',], ['95', 'やっと…', 'リスト作り終わった…'],
        ]
        paginator = Paginator(fruitslist, 20)
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        
        #返却値
        params = {
            'object_list': fruitslist,
            'page': articles, 
        }
        return render(request, "fruitslist.html", params)




class FruitsView(TemplateView):
    template_name = 'fruits.html'
    ins = FruitsData()

    def get(self, request):
        params = {
            'object_list': self.ins.data_list()
        }
        return render(request, 'fruits.html', params)


class FruitsCreateView(FruitsView):
    def get(self, request):
        param = {
            'form': FruitsForm()
        }
        return render(request, 'fruitscreate.html', param)

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        memo = request.POST.get('memo')

        form = FruitsForm(request.POST)

        if not form.is_valid():
            param = {
                'form': FruitsForm(request.POST)
            }
            return render(request, 'fruitscreate.html', param)
        
        self.ins.data_set(id, name, memo)

        return redirect('web:fruits')
        
        
class FruitsDetailView(FruitsView, APIView):
    def get(self, request, id):
        param = {
            'form': FruitsForm(self.ins.data_get(id)),
            'id': id,
        }
        return render(request, 'fruitsupdate.html', param)

    def put(self, request, id):
        form = FruitsForm(request.POST)

        if not form.is_valid():
            param = {
                'form': FruitsForm(request.POST)
            }
            return render(request, 'fruitsupdate.html', param)

        id = self.cleaned_data['id']
        name = self.cleaned_data['name']
        memo = self.cleaned_data['memo']

        print(id)
        print(memo)

        param = {
            "object_list": self.ins.data_update(id, name, memo),
        }
        return Response(param)

    def delete(self, request, id):
        param = {
            "object_list": self.ins.data_delete(id),
        }
        return Response(param)



# class FruitsDeleteView(FruitsView, APIView):
#     def get(self, request, id):
#         param = {
#             "object_list": self.ins.data_get(id),
#         }
#         return Response(param)

#     def delete(self, request, id):
#         param = {
#             "object_list": self.ins.data_delete(id),
#         }
#         return Response(param)
        
        
# class FruitsUpdateView(FruitsView, APIView):
#     def get(self, request, id):
#         param = self.ins.data_get(id)
#         return Response(param)

#     def put(self, request, id):
#         id = request.data['id']
#         name = request.data['name']
#         memo = request.data['memo']

#         param = {
#             "object_list": self.ins.data_update(id, name, memo),
#         }

#         return Response(param)