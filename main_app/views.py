from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User






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
            context["header"] = f"Searching for {name}"
        else:
            context["cars"] = Car.objects.all()
            context["header"] = "Our Cars"
        return context

# create View

class Car_Create(CreateView):
    model = Car
    fields = ['name', 'img', 'year', 'color']
    template_name = "car_create.html"
    success_url = "/cars/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cars')

#detail view

class CarDetail(DetailView):
    model = Car
    template_name = "car_detail.html"

#update view

class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'img', 'year', 'color']
    template_name = "car_update.html"
    
    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})

#delete view

class CarDelete(DeleteView):
    model = Car
    template_name = "car_delete_confirmation.html"
    success_url = "/cars/"

#user

# add this new view function

def profile(request, username):
    user = User.objects.get(username=username)
    cars = Car.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cars': cars})