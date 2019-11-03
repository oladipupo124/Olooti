from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Event


class Event(ListView):
    template_name = " " #Victor add the template
    model = Event
    queryset = Event.objects.all()
