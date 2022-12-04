from django.contrib import admin

from books.models import Book, Loan
 
admin.site.register(Book)
admin.site.register(Loan)


