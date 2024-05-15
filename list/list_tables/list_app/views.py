from django.shortcuts import render, redirect
from .models import Book
# Create your views here.


def createbook(request):
    books = Book.objects.all()
    if request.method == "POST":

        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book = Book(title=title, author=author, price=price)

        book.save()

    return render(request, 'book.html', {'books': books})


def listbook(request):
    books = Book.objects.all()

    return render(request, 'list.html', {'books': books})


def detailsbook(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, 'details.html', {'book': book})


def updatebook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":

        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book.title = title
        book.author = author
        book.price = price

        book.save()
        return redirect('/')

    return render(request, 'update.html', {'book': book})


def deletebook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('/')

    return render(request, 'delete.html', {'book': book})


def index(request):
    return render(request, 'base.html')


def createauthor(request):

    return render(request, 'forms.py')
