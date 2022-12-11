from django.contrib import admin
from books.models import Book,Authors,BookReview
 
admin.site.register(Book)
admin.site.register(Authors)
=======
from books.models import Book,Author
 
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookReview)


