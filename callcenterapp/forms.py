from django import forms
from .models import Book

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['chindi', 'cenglish']
