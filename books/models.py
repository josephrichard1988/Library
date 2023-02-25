from django.db import models
from author import models as author_model

# Create your models here.


class publishers(models.Model):
    publisher_name = models.CharField(max_length=20, unique=True)
    publisher_contact = models.CharField(max_length=300)
    publisher_address = models.CharField(max_length=300)

    def __str__(self):
        return self.publisher_name


class books(models.Model):
    book_name = models.CharField(max_length=20)
    book_desc = models.CharField(max_length=300)
    book_genre = models.CharField(max_length=30)
    book_publisher = models.ForeignKey(
        publishers, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book_name


class author_books(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    author = models.ForeignKey(
        author_model.author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book_name
