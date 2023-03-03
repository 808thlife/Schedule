from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic

import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm
# Create your views here.

class CalendarView():
    pass

@login_required(login_url="accounts:index")
def index(request):
    return render(request, 'app/calendar.html')    

@login_required(login_url="accounts:index")
def calendar(request):
    pass

@login_required(login_url="accounts:index")
def event_new(request):
    return render(request, "app/event.html")
