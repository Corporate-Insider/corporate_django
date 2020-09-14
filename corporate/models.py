from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from accounts.models import User
        
class Company(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    review = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')

    def __str__(self):
        return f'{self.review}'
class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', related_query_name='rating')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='ratings', related_query_name='rating')
