from django.shortcuts import render
from .models import Car, Driver, Crew

def table_all(request):
    cars = Car.objects.all()
    drivers = Driver.objects.all()
    crews = Crew.objects.all()
    return render(request, 'cars/table_all.html', {'cars': cars, 'drivers': drivers, 'crews': crews})
