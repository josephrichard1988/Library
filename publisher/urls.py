from django.contrib import admin
from django.urls import path
from publisher import views as publisher_view

urlpatterns = [
    path('create-publisher-page', publisher_view.create_publisher_page_fn,
         name="create_publisher_page"),
]
