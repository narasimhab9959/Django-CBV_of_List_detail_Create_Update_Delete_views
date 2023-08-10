from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from app.models import *
from django.urls import reverse_lazy

class SchoolList(ListView):
    model=School 
    context_object_name='allSO'

class SchoolDetails(DetailView):
    model=School
    context_object_name='DOSI'
   
class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='dso'
    success_url=reverse_lazy('SchoolList')   # this one for taking back to List of objects...
    
