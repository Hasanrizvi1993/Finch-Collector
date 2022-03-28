from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views import View
from .models import Car, CarType
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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
@method_decorator(login_required, name='dispatch')
class Car_Create(CreateView):
    model = Car
    fields = ['name', 'img', 'year', 'color', 'cartypes']
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
@method_decorator(login_required, name='dispatch')
class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'img', 'year', 'color', 'cartypes']
    template_name = "car_update.html"
    
    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})

#delete view
@method_decorator(login_required, name='dispatch')
class CarDelete(DeleteView):
    model = Car
    template_name = "car_delete_confirmation.html"
    success_url = "/cars/"

#user

# add this new view function
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    cars = Car.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cars': cars})



#CARTYPE VIEWS

def cartypes_index(request):
    cartypes = CarType.objects.all()
    return render(request, 'cartype_index.html', {'cartypes': cartypes})

def cartypes_show(request, cartype_id):
    cartype = CarType.objects.get(id=cartype_id)
    return render(request, 'cartype_show.html', {'cartype': cartype})

@method_decorator(login_required, name='dispatch')
class CarTypeCreate(CreateView):
    model = CarType
    fields = '__all__'
    template_name = "cartype_form.html"
    success_url = '/cartypes/'

@method_decorator(login_required, name='dispatch')
class CarTypeUpdate(UpdateView):
    model = CarType
    fields = ['type']
    template_name = "cartype_update.html"
    success_url = '/cartypes/'

@method_decorator(login_required, name='dispatch')
class CarTypeDelete(DeleteView):
    model = CarType
    template_name = "cartype_confirm_delete.html"
    success_url = '/cartypes/'



# django auth
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cars')

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})