from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Car


# Create your views here.
class Home(TemplateView):
    template_name="home.html"


class About(TemplateView):
    template_name = "about.html"


cars = Car.objects.all()

class CarList(TemplateView):
    template_name = 'carlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = cars # this is where we add the key into our context object for the view to use
        return context

