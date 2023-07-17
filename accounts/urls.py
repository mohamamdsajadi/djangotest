
from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.LoginView.as_view() , name ='login'),
    path('logout/' , views.LogOutView.as_view() , name='logout'),
    path('welcome/',views.Welcome.as_view() , name='welcome'),
    path('signup/' , views.CreateUser.as_view() , name= 'signup') ,

    
]
