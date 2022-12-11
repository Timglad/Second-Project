from django.contrib import admin
from books.models import Book,Authors,BookReview
 
admin.site.register(Book)
admin.site.register(Authors)
admin.site.register(BookReview)


