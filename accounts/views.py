import imp

from re import template
from telnetlib import LOGOUT
from tkinter import N
from unittest.mock import patch
from django.shortcuts import render
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm 
from  .Forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic 
from django.urls import reverse_lazy
class LoginView(generic.FormView) : 
    form_class = AuthenticationForm
    success_url = reverse_lazy("welcome")
    template_name = "accounts/login_form.html"
    def get_form(self , form_class = None) : 
        if form_class is None :
            form_class = self.get_form_class()
        return form_class(self.request , **self.get_form_kwargs())
    def form_valid(self,form ) :
        login(self.request , form.get_user()) 
        return super().form_valid(form)

# Create your views here.
class Welcome(LoginRequiredMixin,generic.TemplateView):
    template_name = "accounts/welcome.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_name"] = self.request.user.username 
        return context
class LogOutView (generic.RedirectView):
    url = reverse_lazy("login")    
    
    def get(self, request, *args, **kwargs) :
         logout(request)
         return super().get(request, *args, **kwargs)
     
     
class CreateUser(generic.CreateView):
    template_name = "accounts/register.html"    
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    