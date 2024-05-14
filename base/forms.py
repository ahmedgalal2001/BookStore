from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'image', 'price', 'genre', 'rating', 'categories', 'isbn',  'views', 'description']
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10 or len(title) > 50:
            raise forms.ValidationError("The title must be between 10 and 50 characters.")
        return title
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("The category name must be at least 2 characters long.")
        return name