import email
from operator import mod
from pydoc import describe
from pyexpat import model
from re import S, U
from turtle import title
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser , BaseUserManager , PermissionsMixin )

# Create your models here.
from django.utils import timezone


# class UserManager(BaseUserManager) :
#     def create_user(self,email , username ,display_name = None , password = None ):
#         if not email:
#             raise ValueError("the user must have an email address")
#         if not display_name :
#             display_name = username
        
#         user = self.model (
#             email = self.normalize_email(email) ,
#             username = username ,
#             display_name = display_name
#         )
#         user.set_password(password)
#         user.save()
#         return user
        
        
#     def create_superuser(self,email , username ,display_name = None , password = None ):  
#         user = self.create_user(email,username , display_name , password)  
#         user.is_staff = True
#         user.is_superuser = True   
#         user.save()
#         return user
            
# class User(AbstractBaseUser ,PermissionsMixin ):
#     email  = models.EmailField(unique = True)
#     username = models.CharField(max_length=44 , unique=True)
#     display_name = models.CharField(max_length=140)
#     avatar  = models.ImageField(blank = True , null = True )
#     date_joined = models.DateTimeField(default = timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     objects = UserManager()
    
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELD  = [ "username" , "display_name"]
    
#     def  __str__(self):
#          return "@{}".format(self.username)
     
#     def get_short_name (self):
#         return self.display_name
#     def get_long_name (self) :
#         return "{} @{}".format( self.display_name , self.username)
    
    
    

    

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True, )
    description = models.TextField()
   
    def __str__(self):
        return self.title
    
    

   
    


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
