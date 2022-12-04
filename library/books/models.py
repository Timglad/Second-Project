from enum import Enum
from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.

class BookType(Enum):
   ten_days = 1
   five_days = 2
   two_days = 3

class LoanStatus(Enum):
   available = 1
   loaned = 2

class Book(models.Model):

   class BookType2(models.IntegerChoices):
      ten_days = 10, "Ten Days Loan"
      five_days = 5, "Five Days Loan"
      two_days = 2, "Two Days Loan"
   
   class LoanStatus2(models.TextChoices):
      LOANED = 'L', 'Loaned'
      AVAILABLE = 'A', 'Available'


   name = models.CharField(max_length=40, null=False)
   author = models.CharField(max_length=40, null=False)
   year_published = models.DateField(default="Unknown")
   type = models.SmallIntegerField(null=False, default = BookType.two_days, choices=BookType2.choices)
   image = models.ImageField(null=True, blank=True, default='/placeholder.png')
   status =models.CharField(max_length=40, null=False, default= LoanStatus2.AVAILABLE, choices= LoanStatus2.choices)

   


   def __str__(self):
    return self.name + "," + self.author

class Loan(models.Model):
    custID = models.ForeignKey(User, on_delete=models.CASCADE)
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    loandate = models.DateField(auto_now_add=True)
    returndate = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.custID + "," + self.returndate


