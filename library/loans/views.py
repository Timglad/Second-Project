from django.shortcuts import render,redirect
from books.models import Book
from loans.models import Loan
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date, timedelta

# Create your views here.

@login_required
def loans(request, pk):
    current_book = Book.objects.get(id=pk)
    if current_book.status == "A":
        current_user = request.user
        loan = Loan(custID = current_user, bookID= current_book)
        loan.save()
        loantype = current_book.type
        loan.returndate = loan.loandate + timedelta(days=loantype)
        loan.save()
        current_book.status = "L"
        current_book.save()
        return redirect('books:mains')
    return redirect('books:mains')

@login_required
def returns(request, pk):
    current_loan = Loan.objects.get(id=pk)
    book = Book.objects.get(id=current_loan.bookID.id)
    book.status = "A"
    book.save()
    current_loan.delete()
    return redirect('loans:loans')

def late_check(pk):
    loan = Loan.objects.get(id = pk)
    current_date = date.today()
    if loan.returndate < current_date:
        loan.status = "O"
    else:
        loan.status = "V"
    loan.save()

@login_required
def loan_list_private(request):
    loans = Loan.objects.all()
    current_user = request.user
    loans_private = [{}]
    for loan in loans:
        late_check(loan.id)
        if loan.custID == current_user:
            loans_private.append(loan)
        else :
             messages.info(request,"Saved Successfuly")

    context = {
        'loan_list': loans_private[1:],
    }
    return render(request, 'loans.html', context=context)
@staff_member_required
def loan_list(request):
    loans = Loan.objects.all()
    context = {
       'loan_list': loans,
    }
    return render(request,'loans.html',context=context)

@staff_member_required
def late_loans(request):
    loans = Loan.objects.all()
    late_loan = [{}]
    for loan in loans:
        late_check(loan.id)
        if loan.status == "O":
            late_loan.append(loan)
    context ={
        'loan_list': late_loan[1:],
    }
    return render(request, 'loans.html',context=context)

def test_table(request):
    return render(request,'tables.html')

