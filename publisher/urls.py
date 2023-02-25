from django.contrib import admin
from django.urls import path
from publisher import views as publisher_view

urlpatterns = [
    path('create-publisher-page', publisher_view.create_publisher_page_fn,
         name="create_publisher_page"),
    path('update-publisher-page/<int:publisher_id>', publisher_view.update_publisher_page_fn,
         name="update_publisher_page"),
    path('delete-publisher-page/<int:publisher_id>', publisher_view.delete_publisher_page_fn,
         name="delete_publisher_page"),
]
