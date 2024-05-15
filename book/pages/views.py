from django.shortcuts import render
from .models import Book
# Create your views here.


def create_book(request):
    books = Book.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book = Book(title=title, author=author, price=price)

        book.save()

    return render(request, 'book.html', {'books': books})


def list_book(request):
    books = Book.objects.all()

    return render(request, 'list.html', {'books': books})
