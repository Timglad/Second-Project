from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.models import Book
 

def mains(request):
   mybooks = Book.objects.all()
   context = {
       'book_list': mybooks,
   }
   return render(request,'mains.html',context=context)