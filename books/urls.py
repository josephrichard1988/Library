from django.contrib import admin
from django.urls import path
from books import views as book_view

urlpatterns = [
    path('create-book-page', book_view.create_book_page_fn ,name="create_book_page"),
]