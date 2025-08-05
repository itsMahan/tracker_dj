from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from tracker_app.forms import TrackerUpdateForm
from .forms import CounterUpdateForm
from .models import Counter


# Create your views here.


def list_counters(request):
    counters = Counter.objects.all()

    return render(request, 'counter_app/list_counters.html', {'counters': counters})


def add_counter(request):
    if request.method == 'POST':
        name = request.POST['name']
        start_date = request.POST['start_date']
        counter_obj = Counter(name=name, start_date=start_date)
        counter_obj.save()
        return redirect('list_counters')

    return render(request, 'counter_app/add_counter.html')


def delete_counter(request, id):
    Counter.objects.get(id=id).delete()
    messages.success(request, 'Counter deleted successfully')
    return redirect('home')

def reset_counter(request, id):
    counter = Counter.objects.get(id=id)
    counter.start_date = datetime.now()
    counter.save()
    messages.success(request, 'Counter reset from Today')
    return redirect('home')

def update_counter(request, id):
    if request.method == 'POST':
        form = CounterUpdateForm(request.POST, instance=Counter.objects.get(id=id))
        if form.is_valid():
            messages.success(request, 'Counter updated successfully')
            form.save()
            return redirect('list_counters')
    else:
        form = CounterUpdateForm(instance=Counter.objects.get(id=id))
    return render(request, 'counter_app/counter_update_form.html', {'form': form})