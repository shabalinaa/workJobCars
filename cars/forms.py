from django import forms
from .models import Car, Driver, Crew

class CarsForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('color', 'number', 'model',)

class DriversForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('fio', 'experience',)

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ('name', 'driver', 'car')