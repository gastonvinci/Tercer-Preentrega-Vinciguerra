from django.urls import path
from .views import home, add_author, add_book, add_publisher, author_list, book_list, publisher_list

urlpatterns = [
    path('', home, name='home'),
    path('author/add/', add_author, name='add_author'),
    path('book/add/', add_book, name='add_book'),
    path('publisher/add/', add_publisher, name='add_publisher'),
    path('authors/', author_list, name='author_list'),
    path('books/', book_list, name='book_list'),
    path('publishers/', publisher_list, name='publisher_list'),
]
