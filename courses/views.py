import imp
from turtle import title
from django.shortcuts import render
from django.urls import reverse_lazy
import courses
from .models import Course
from courses import models
from django.views.generic import ListView , CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# def course_list(request):
#   try:
#       Course.objects.create(title='4' , description = '2')
#   finally:
# #   Course.objects.create(title='2' , description = '3')
#    courses = list(Course.objects.all())
#    return render(request , 'courses/course_list.html' , {'courses' : courses})


class CourseListView(ListView):
  queryset = Course.objects.order_by("-title")
  

class CourseCreateView(LoginRequiredMixin,CreateView)  :
  model = Course 
  fields = ["title" , "description" ] 
  template_name = "courseform.html"
  success_url = reverse_lazy('list')

  def form_valid(self,form):
      form.instance.user = self.request.user 
      messages.success(self.request , "yayyyyy its worked")
      return super(CourseCreateView , self).form_valid(form)
      
    
  