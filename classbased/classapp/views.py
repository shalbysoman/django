from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from django.views.generic import CreateView, ListView
# Create your views here.


class BookCreateView(CreateView):
    model = Book
    template_name = 'create.html'
    fields = ['title', 'author', 'price']
    success_url = reverse_lazy('booklist')

class BookListView(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'books'


