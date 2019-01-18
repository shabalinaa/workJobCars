from django.shortcuts import render
from .models import Car, Driver, Crew
from .forms import CarsForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

def table_all(request):
    cars = Car.objects.all()
    drivers = Driver.objects.all()
    crews = Crew.objects.all()
    return render(request, 'cars/table_all.html', {'cars': cars, 'drivers': drivers, 'crews': crews})


def car_new(request):
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('table_all')
    else:
        form = CarsForm()
    return render(request, 'cars/car_edit.html', {'form': form})

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarsForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('table_all')
    else:
        form = CarsForm(instance=car)
    return render(request, 'cars/car_edit.html', {'form': form})

# удаление данных из бд
def car_delete(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        car.delete()
        return HttpResponseRedirect("/")
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

