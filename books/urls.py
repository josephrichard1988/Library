from django.contrib import admin
from django.urls import path
from books import views as book_view

urlpatterns = [
    path('create-book-page', book_view.create_book_page_fn, name="create_book_page"),
    path('view-book-page/<int:book_id>',
         book_view.view_book_page_fn, name="view_book_page"),
    path('home-page/<int:book_id>', book_view.home_page_fn, name="home_page"),
]
