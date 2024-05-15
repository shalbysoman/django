from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name='booklist'),
    path('createview/', views.BookCreateView.as_view(), name='createbook'),
]