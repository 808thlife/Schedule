from django.urls import path
from . import views

#FOR CORE APP
app_name = "scheduleapp"

urlpatterns = [
    path("", views.index, name = 'index'),
    path("calendar", views.calendar, name = "calendar"),
    path("add", views.event_new, name = "new_event"),
]
