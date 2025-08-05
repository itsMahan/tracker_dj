from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TrackerUpdateForm
from .models import Tracker


def list_trackers(request):
    trackers = Tracker.objects.all()

    return render(request, 'tracker_app/list_tracker.html', {'trackers': trackers})


def add_tracker(request):
    if request.method == 'POST':
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        tracker_obj = Tracker(name=name, start_date=start_date, end_date=end_date)
        tracker_obj.save()
        return redirect('http://127.0.0.1:8000/tracker/list')

    return render(request, 'tracker_app/add_tracker.html')


def delete_tracker(request, id):
    Tracker.objects.get(id=id).delete()
    messages.success(request, 'Tracker deleted successfully')
    return redirect('list_trackers')

def update_tracker(request, id):
    tracker = Tracker.objects.get(id=id)
    if request.method == 'POST':
        form = TrackerUpdateForm(request.POST, instance=tracker)
        if form.is_valid():
            messages.success(request, 'Tracker updated successfully')
            form.save()
            return redirect('list_trackers')
    else:
        form = TrackerUpdateForm(instance=tracker)
    return render(request, 'tracker_app/tracker_update_form.html', {'form': form})
