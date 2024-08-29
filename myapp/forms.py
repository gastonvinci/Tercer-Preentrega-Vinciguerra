from django import forms
from .models import Author, Book, Publisher

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'publisher']  

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
