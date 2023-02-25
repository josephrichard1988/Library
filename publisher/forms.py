from django.core import validators
from django import forms
from books import models as book_models


class publishersForm(forms.ModelForm):
    class Meta:
        model = book_models.publishers
        fields = '__all__'
