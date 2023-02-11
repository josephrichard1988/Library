from django.core import validators
from django import forms
from .models import books


class booksForm(forms.ModelForm):
    class Meta:
        model = books
        fields = '__all__'
        '''
        labels = {
            'room_type': 'Room Type',
            'room_type_desc': 'Room Type Description',
        }
        help_text = {'room_type': 'Enter The Room Type',
                     'room_type_desc': 'Enter the Type Description'}
        error_messages = {'room_type': {'required': 'Enter The Room Type'},
                          'room_type_desc': {'required': 'Enter the Type Description'}}
        widgets = {'room_type': forms.TextInput(attrs={"class": "form-control", "style": "width: 100%; margin-bottom: 20px;", "placeholder": "Room Type"}),
                   'room_type_desc': forms.Textarea(attrs={"class": "form-control", "style": "width: 100%", "placeholder": "Room Type Description", "rows": 3})}
        '''