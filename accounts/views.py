import imp

from re import template
from tkinter import N
from unittest.mock import patch
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from django.views import generic 
from django.urls import reverse_lazy
class LoginView(generic.FormView) : 
    form_class = AuthenticationForm
    success_url = reverse_lazy('list')
    template_name = "accounts/login_form.html"
    def get_form(self , form_class = None) : 
        if form_class is None :
            form_class = self.get_form_class()
        return form_class(self.request , **self.get_form_kwargs())
    def form_valid(self,form ) :
        login(self.request , form.get_user()) 
        return super().form_valid(form)

# Create your views here.
class Welcome(generic.TemplateView):
    template_name = 'accounts/welcome.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_name"] = self.request.user.username 
        return context
    