from django.shortcuts import render
from tracker_app.models import Tracker
from counter_app.models import Counter
from event_app.models import Event



def home(request):
    return render(request, 'home_app/home.html')

def show_all(request):
    context = {
        'trackers': Tracker.objects.all(),
        'events': Event.objects.all(),
        'counters': Counter.objects.all(),
    }
    return render(request, 'home_app/show_all.html', context)