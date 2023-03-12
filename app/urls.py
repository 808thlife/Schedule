from django.urls import path
from . import views

#FOR CORE APP
app_name = "scheduleapp"

urlpatterns = [
    path("", views.index, name = 'index'),
    path("profile/", views.index, name = "profile"),
    path("about/", views.about, name = "about"),
    path("add/", views.addingMenu, name = "adding"),
    path("add-student/", views.addStudent, name = "addStudent"),
    path("<int:year_id>", views.deleteStudent, name = "deleteStudent"),
    path("add-lesson/", views.addLesson, name = "addLesson"),
    path("add-teacher/", views.addTeacher, name = "addTeacher"),
    path("add-student/<int:year_id>/", views.viewStudents, name = "viewStudents"),
    path("search", views.search, name = "search")
]
