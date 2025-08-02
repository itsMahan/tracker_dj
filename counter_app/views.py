from datetime import datetime

from django.shortcuts import render, redirect

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
        return redirect('http://127.0.0.1:8000/counter/list')

    return render(request, 'counter_app/add_counter.html')


def delete_counter(request, id):
    Counter.objects.get(id=id).delete()
    return redirect('home')

def reset_counter(request, id):
    counter = Counter.objects.get(id=id)
    counter.start_date = datetime.now()
    counter.save()
    return redirect('home')