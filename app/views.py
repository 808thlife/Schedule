from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic

from datetime import datetime
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
    return render(request,)

@login_required(login_url="accounts:index")
def event_new(request):
    return render(request, "app/event.html")

class CalendarView(generic.ListView):
    model = Lesson
    template_name = 'app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Lesson()
    if event_id:
        instance = get_object_or_404(Lesson, pk=event_id)
    else:
        instance = Lesson()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('scheduleapp:calendar'))
    return render(request, 'accounts/event.html', {'form': form})
