from django.shortcuts import render, redirect
from .models import Event


def list_events(request):
    events = Event.objects.all()

    return render(request, 'event_app/list_event.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        total_events = request.POST['total_events']
        used_events = request.POST['used_events']
        event_obj = Event(name=name, total_events=total_events, used_events=used_events)
        event_obj.save()
        return redirect('http://127.0.0.1:8000/event/list')

    return render(request, 'event_app/add_event.html')


def delete_event(request, id):
    Event.objects.get(id=id).delete()
    return redirect('home')