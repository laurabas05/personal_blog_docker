from django.shortcuts import render
from aboutme.models import Person

def homepage(request):
    person_list = Person.objects.all()
    return render(request, 'home.html', {'persons': person_list})