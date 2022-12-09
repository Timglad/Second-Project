from django.shortcuts import render,redirect
from books.forms import BookForm
from django.contrib.auth.decorators import login_required
from books.models import Book
from django.contrib import messages
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required


def read_mains():
    with open("final_rank.csv") as book_file:
        book_file.readline()
        for line in book_file:
            my_list = line.split(",")
            book = Book(
                name = my_list[0],
                author = my_list[1],
                year_published = my_list[2],
                type = my_list[3],
                image = my_list[4],
                status = my_list[5]
            )
            print(book)
            book.save()
    return book

def mains(request):
    #read_mains()
    mybooks = Book.objects.all()
    context = {
       'book_list': mybooks,
   }
    return render(request,'mains.html',context=context)

@staff_member_required
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

@staff_member_required
def delete_book(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('books:mains')

def single_book(request, pk):
    book = Book.objects.get(id=pk)
    return render(request,'single_book.html',{'book':book})

@staff_member_required
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





    

    





    
