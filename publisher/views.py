from django.shortcuts import render, redirect
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
    return render(request, "publishers/manage_publisher.html", data)


def update_publisher_page_fn(request, publisher_id):
    print(publisher_id)
    publisher = book_model.publishers.objects.get(id=publisher_id)
    publisher_form = publishersForm(instance=publisher)

    if request.method == "POST":
        publisher_form_submit = publishersForm(
            request.POST, instance=publisher)
        if publisher_form_submit.is_valid():
            publisher_form_submit.save()
            return redirect('create_publisher_page')

    publisher_table_data = book_model.publishers.objects.all()
    data = {
        'publisher_form': publisher_form,
        'publisher_table_data': publisher_table_data
    }
    return render(request, "publishers/manage_publisher.html", data)


def delete_publisher_page_fn(request, publisher_id):
    publisher = book_model.publishers.objects.get(id=publisher_id)
    publisher.delete()
    return redirect('create_publisher_page')
