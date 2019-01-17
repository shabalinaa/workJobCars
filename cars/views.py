from django.shortcuts import render

def table_all(request):
    return render(request, 'cars/table_all.html', {})
