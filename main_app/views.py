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

# class CarList(TemplateView):
#     template_name = 'carlist.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["cars"] = cars # this is where we add the key into our context object for the view to use
#         return context

class CarList(TemplateView):
    template_name = 'carlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["cars"] = Car.objects.filter(name__icontains=name)
        else:
            context["cars"] = Car.objects.all()
        return context