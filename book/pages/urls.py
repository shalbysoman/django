from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book),
    path('listview/', views.list_book)
]
