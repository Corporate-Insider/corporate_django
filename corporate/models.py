from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from accounts.models import User

# Create your models here.

# class UserManager(BaseUserManager):
#     """Manager for user profiles"""

  
#     def create_user(self, email, name, password=None, **extra_fields):
#         """Create a new user profile"""
#         # Add a custom validation error
#         if not email:
#             raise ValueError('User must have an email address')

       
#         user = self.model(email=self.normalize_email(email), name=name, **extra_fields)

#         # Use the set_password method to hash the password
#         user.set_password(password)
#         user.save()

#         return user

#     def create_superuser(self, email, name, password):
#         """Create and save a new superuser with given details"""
#         user = self.create_user(email, name, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()

#         return user

#         # Inherit from AbstractBaseUser and PermissionsMixin:
# class User(AbstractBaseUser, PermissionsMixin):
#     """Database model for users"""
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         """Return string representation of the user"""
#         return self.email
        
class Company(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    rated = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')

    def __str__(self):
        return f'{self.review}'