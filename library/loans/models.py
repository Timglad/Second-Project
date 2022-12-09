from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.


class LoanStatus(Enum):
   available = 1
   loaned = 2



class Loan(models.Model):
    class LoanTime(models.TextChoices):
       OVERTIME = 'O', 'Late Return'
       ONTIME = 'V' , 'Good'

    custID = models.ForeignKey(User, on_delete=models.CASCADE)
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    loandate = models.DateField(auto_now_add=True)
    returndate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=40, null=False, default= LoanTime.ONTIME, choices=LoanTime.choices)

    def __str__(self):
      return f'{self.custID} - {self.returndate}'

