from django.db import models
from django.shortcuts import render,HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from .models import Student,School

class Schoollist(ListView):
    context_object_name='schools'
    model=models.School

class Studentdetails(DetailView):
    model=models.Student 
    template_name='app1/school.html'



    

    

