from django.forms import ModelForm
from books.models import Book,Authors

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year_published', 'type', 'image'] 


class AuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = ['name','age', 'nationality'] 



