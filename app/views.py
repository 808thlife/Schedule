from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django import forms

from .models import User, Students, Lesson

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

#adding students
def addStudent(request):
    if request.method == "POST":
        year = request.POST["year"]
        faculty = request.POST["faculty"]
        number = request.POST["group_number"]
        f = Students(group_year = year, group_title = faculty, group_number = number)
        f.save()
    return render(request, "app/AddingForms/addStudents.html")

#viewing
def viewStudents(request, year_id):
    arr = Students.objects.all()
    context = {"year_id":year_id, 'students':arr}
    return render(request, "app/AddingForms/Studentslist.html", context)

def addLesson(request):
    context = {}
    return render(request, "app/AddingForms/addLesson.html")

def addTeacher(request):
    context = {}
    return render(request, "app/AddingForms/addTeacher.html")