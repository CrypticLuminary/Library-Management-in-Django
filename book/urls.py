from django.urls import path
from .views import *

app_name = "book"
urlpatterns = [
    path('add_book/', AddBook, name = "add_book"),
    path('book_list/', BookList, name = "book_list"),
]
