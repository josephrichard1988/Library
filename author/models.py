from django.db import models

# Create your models here.
class author(models.Model):
    author_fname = models.CharField(max_length=20, default="Abcd")
    author_lname = models.CharField(max_length=20)
    author_address = models.CharField(max_length=300)
    author_contact = models.CharField(max_length=30)
    def __str__(self):
        return self.author_fname