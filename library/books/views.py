from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from books.forms import BookForm
from django.contrib.auth.decorators import login_required
from books.models import Book, Loan
from django.contrib import messages
from django.db.models import Q
#from django.contrib.auth.models import User
from django.db import models
import datetime

def mains(request):
   mybooks = Book.objects.all()
   context = {
       'book_list': mybooks,
   }
   return render(request,'mains.html',context=context)

def add_book(request):
    if request.method == "POST":
        bookform = BookForm(request.POST, request.FILES)
        if bookform.is_valid():
            bookform.save()
            return redirect('books:mains')          
    else:
        bookform = BookForm()
   
    context = {
        'bookform': bookform,
    }
    return render(request, "add_book.html", context=context)
        
def search_books(request):
    search = request.GET.get('search')
    books = Book.objects.filter(Q(name__contains= search) | Q(author__contains= search))
    context = {
        'book_list' : books,
    }
    return render(request, 'mains.html', context= context)

def delete_book(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('books:mains')

def single_book(request, pk):
    book = Book.objects.get(id=pk)
    return render(request,'single_book.html',{'book':book})

def edit_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "GET":
        return render(request,'single_book.html',{'book':book,'edit':True})
    book.name = request.POST.get('name')
    book.author = request.POST.get('author')
    book.year_published = request.POST.get('yearpublished')
    book.save()
    messages.info(request,"Saved Successfuly")
    return redirect('books:mains')


def loans(request, pk):
    current_book = Book.objects.get(id=pk)
    if current_book.status == "A":
        current_user = request.user
        loan = Loan(custID = current_user, bookID= current_book)
        loan.save()
        loantype = current_book.type
        loan.returndate = loan.loandate + datetime.timedelta(days=loantype)
        loan.save()
        current_book.status = "L"
        current_book.save()
        return redirect('books:mains')
    return redirect('books:mains')

def returns(request, pk):
    current_loan = Loan.objects.get(id=pk)
    book = Book.objects.get(id=current_loan.bookID.id)
    book.status = "A"
    book.save()
    current_loan.delete()
    return redirect('books:loans')

def loan_list(request):
    loans = Loan.objects.all()
    current_user = request.user
    loans_private = [{}]
    for loan in loans:
        if loan.custID == current_user:
            loans_private.append(loan)
        else :
             messages.info(request,"Saved Successfuly")

    context = {
        'loan_list': loans_private[1:],
    }
    return render(request, 'loans.html', context=context)


    





    
