from django.shortcuts import render
from .models import Car, Driver, Crew
from .forms import CarsForm, DriversForm, CrewForm
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
        car = CarsForm(request.POST)
        if car.is_valid():
            post = car.save(commit=False)
            post.save()
            return redirect('table_all')
    else:
        car = CarsForm()
    return render(request, 'cars/car_edit.html', {'car': car})

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car_form = CarsForm(request.POST, instance=car)
        if car_form.is_valid():
            car = car_form.save(commit=False)
            car.save()
            return redirect('table_all')
    else:
        car_form = CarsForm(instance=car)
    return render(request, 'cars/car_edit.html', {'car': car_form})

# удаление данных из бд
def car_delete(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        car.delete()
        return HttpResponseRedirect("/")
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

'''обработка для Вoдителей'''

def driver_new(request):
    if request.method == "POST":
        driver = DriversForm(request.POST)
        if driver.is_valid():
            post = driver.save(commit=False)
            post.save()
            return redirect('table_all')
    else:
        driver = DriversForm()
    return render(request, 'cars/drivers_edit.html', {'driver': driver})

def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        driver_forms = DriversForm(request.POST, instance=driver)
        if driver_forms.is_valid():
            driver = driver_forms.save(commit=False)
            driver.save()
            return redirect('table_all')
    else:
        driver_forms = DriversForm(instance=driver)
    return render(request, 'cars/drivers_edit.html', {'driver': driver_forms})

# удаление данных из бд
def driver_delete(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
        driver.delete()
        return HttpResponseRedirect("/")
    except Driver.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


'''обработка для экипажей'''
def crew_new(request):
    if request.method == "POST":
        crew = CrewForm(request.POST)
        if crew.is_valid():
            post = crew.save(commit=False)
            post.save()
            return redirect('table_all')
    else:
        crew = CrewForm()
    return render(request, 'cars/crew_edit.html', {'crew': crew})

def crew_edit(request, pk):
    crew = get_object_or_404(Crew, pk=pk)
    if request.method == "POST":
        crew_forms = DriversForm(request.POST, instance=crew)
        if crew_forms.is_valid():
            crew = crew_forms.save(commit=False)
            crew.save()
            return redirect('table_all')
    else:
        crew_forms = CrewForm(instance=crew)
    return render(request, 'cars/crew_edit.html', {'crew': crew_forms})

# удаление данных из бд
def crew_delete(request, pk):
    try:
        crew = Crew.objects.get(pk=pk)
        crew.delete()
        return HttpResponseRedirect("/")
    except crew.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")