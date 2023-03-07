from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django import forms

from .models import *

@login_required(login_url="accounts:index")
def index(request):
    return render(request, 'app/index.html')    

@login_required(login_url="accounts:index")
def calendar(request):
    pass

@login_required(login_url="accounts:index")
def profile(request):
    return render(request, "app/profile.html")

@login_required(login_url="accounts:index")
def about(request):
    return render(request, "app/about.html")

def addingMenu(request):
    return render(request, "app/adding.html")
    
def addStudent(request):
    context = {}
    return render(request, "app/AddingForms/addStudents.html", context)

def addLesson(request):
    context = {}
    return render(request, "app/AddingForms/addLesson.html")

def addTeacher(request):
    context = {}
    return render(request, "app/AddingForms/addTeacher.html")