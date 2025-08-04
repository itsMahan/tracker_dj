from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event
from .forms import EventForm


def list_events(request):
    events = Event.objects.all()

    return render(request, 'event_app/list_event.html', {'events': events})

# def add_event(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         total_events = request.POST['total_events']
#         used_events = request.POST['used_events']
#         event_obj = Event(name=name, total_events=total_events, used_events=used_events)
#         event_obj.save()
#         return redirect('list_events')
#
#     return render(request, 'event_app/add_event.html')


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_events')
    else:
        form = EventForm()
    return render(request, 'event_app/event_form.html', {'form': form})

def delete_event(request, id):
    Event.objects.get(id=id).delete()
    messages.success(request, 'Event deleted successfully')
    return redirect('home')