from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, null=True, default='Joe Joe')
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    city = models.CharField(max_length=20, null=True, default='Tel Aviv')
    age = models.SmallIntegerField(null=True, default=12)

    def __str__(self):
        return f'{self.fullname}, {self.city}'
