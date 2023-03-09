from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
        if Students.objects.filter(group_year = year, group_title = faculty, group_number = number).exists():
            messages.error(request,"This group already exists.")
        else:
            f = Students(group_year = year, group_title = faculty, group_number = number)
            f.save()
    return render(request, "app/AddingForms/addStudents.html")

def deleteStudent(request, year_id):
    relevant_student = Students.objects.get(id = year_id)
    if request.method == "POST":
        Students.objects.filter(id = year_id).delete()
    return HttpResponseRedirect(reverse("scheduleapp:viewStudents", kwargs={"year_id":relevant_student.group_year}))

#viewing
def viewStudents(request, year_id):
    #mh,tmuh, telecom, art
    arr = Students.objects.filter(group_year = year_id).order_by("group_title")
    context = {'students':arr,}
    return render(request, "app/AddingForms/Studentslist.html", context)

def addLesson(request):
    context = {}
    return render(request, "app/AddingForms/addLesson.html")

def addTeacher(request):
    context = {}
    return render(request, "app/AddingForms/addTeacher.html")