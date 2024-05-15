from django.urls import path
from . import views

urlpatterns = [
    path('create-book/', views.createbook, name='create'),
    path('', views.listbook, name='list'),
    path('author/', views.createauthor, name='author'),
    path('detailsview/<int:book_id>/', views.detailsbook, name='details'),
    path('updateview/<int:book_id>/', views.updatebook, name='update'),
    path('deleteview/<int:book_id>/', views.deletebook, name='delete'),
    path('index/', views.index),
]
