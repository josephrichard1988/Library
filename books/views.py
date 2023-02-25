from django.shortcuts import render
from .forms import booksForm

# Create your views here.


def create_book_page_fn(request):
    book_form = booksForm()
    data = {
        'book_form': book_form
    }
    return render(request, "books/create_book_page.html", data)


def view_book_page_fn(request, book_id):
    data_dict = {"book_id": book_id,
                 "book_name": "Happy Potter"}
    return render(request, "books/view_book_page.html", data_dict)


def home_page_fn(request, book_id):
    # Mysql query to DB
    data_dict = {
        "book_id": book_id,
        "book_name": "Happy Potter",
        "to_do_list": ["to_do_1", "to_do_2", "to_do_3", "to_do_4", "to_do_5", "to_do_6"]
    }
    return render(request, "index.html", data_dict)
