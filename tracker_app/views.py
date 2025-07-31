from django.shortcuts import render, redirect
from .models import Tracker


def list_trackers(request):
    trackers = Tracker.objects.all()

    return render(request, 'tracker_app/list_trackers.html', {'trackers': trackers})


def add_tracker(request):
    if request.method == 'POST':
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        tracker_obj = Tracker(name=name, start_date=start_date, end_date=end_date)
        tracker_obj.save()
        return redirect('http://127.0.0.1:8000/tracker/list')

    return render(request, 'tracker_app/add_tracker.html')