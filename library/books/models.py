from enum import Enum
from django.db import models 
from django.contrib.auth.models import User
from users.models import UserProfile
# Create your models here.

class Authors(models.Model):
   name = models.CharField(max_length=40  )
   age = models.IntegerField()
   nationality = models.CharField(max_length=40 )

   def __str__(self):
      return f"{self.name}"


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
   author = models.ForeignKey(Authors,on_delete=models.CASCADE)
   year_published = models.DateField(default="Unknown")
   type = models.SmallIntegerField(null=False, default = BookType.two_days, choices=BookType2.choices)
   image = models.ImageField(null=True, blank=True, default='/placeholder.png')
   status =models.CharField(max_length=40, null=False, default= LoanStatus2.AVAILABLE, choices= LoanStatus2.choices)
   
   def get_rating(self):
         total = sum(int(review['stars']) for review in self.reviews.values())
         if total == 0:
            return total
         else:
            return total / self.reviews.count()
   
   def __str__(self):
    return f"{self.name} {self.author.name}"

class BookReview(models.Model):
      book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
      customer = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
      content = models.TextField(blank=True, null=True)
      stars = models.IntegerField()
      date_added = models.DateTimeField(auto_now_add=True)  

      





