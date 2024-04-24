from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from teacher.models import Books,Human
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View

# Create your views here.
def teacher(request):
    return render(request,'tec/home.html')

class Bookcreateview(CreateView):
    model=Books
    template_name='tec/add_book.html'
    fields='__all__'
    success_url=reverse_lazy('view_book')

class BookListView(ListView):
    model=Books
    template_name='tec/view_book.html'
    context_object_name='oo'
  

class BookDelete(DeleteView,SuccessMessageMixin):
    model=Books
    template_name='tec/del_book.html'
    success_url=reverse_lazy('view_book')
    success_message='deleted successfully'

class Bookupdate(UpdateView):
    model=Books
    template_name='tec/add_book.html'
    fields='__all__'
    success_url=reverse_lazy('view_book')


class Humanview(View):
    def get(self,request):
        print('my get method')
    def post(self,request):
        print('my post method')      