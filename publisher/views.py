from django.shortcuts import render
from .forms import publishersForm
from books import models as book_model

# Create your views here.


def create_publisher_page_fn(request):
    if request.method == "POST":
        publisher_submit_form = publishersForm(request.POST)
        if publisher_submit_form.is_valid():
            publisher_submit_form.save()

    publisher_form = publishersForm()
    publisher_table_data = book_model.publishers.objects.all()
    data = {
        'publisher_form': publisher_form,
        'publisher_table_data': publisher_table_data
    }
    return render(request, "publishers/create_publisher_page.html", data)
