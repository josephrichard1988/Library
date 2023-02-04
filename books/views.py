from django.shortcuts import render

# Create your views here.

def create_book_page_fn(request):
    return render(request,"books/create_book_page.html")
