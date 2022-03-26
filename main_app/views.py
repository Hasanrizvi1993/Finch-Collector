from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name="home.html"


class About(TemplateView):
    template_name = "about.html"

class Car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color

cars = [
    Car("Ford", 2011, "Red"),
    Car("Toyota", 2008, "Blue"),
    Car("Suzuki", 1984, "Green"),
    Car("Honda", 2020, "Yellow"),
]

class CarList(TemplateView):
    template_name = 'carlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = cars # this is where we add the key into our context object for the view to use
        return context

