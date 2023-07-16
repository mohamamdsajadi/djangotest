from django.shortcuts import render


def helloWolrld(request):
    courses = [{'name' : "farsi" ,    'unit' : [1,2,2,3]} , {'name' : "math" ,    'unit' : [3,6,7]}]
    return  render(request , 'home.html' , {'courses' : courses})
    
# def course_list(request):
#      context={
#          "course_name" : "farsi",
#          "list" : [1,2,3,4,5,6,7]
#      }
#      return render(request ,'courses/course_list.html' , context)
    
# # Create your views here.
# def helloWorld(request):
#     return render(request , 'home.html' )