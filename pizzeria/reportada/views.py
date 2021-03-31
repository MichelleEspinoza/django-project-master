from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
def index(request):
    return render(request, 'reportada/index.html')

def sucursales(request):
    return render(request, 'reportada/sucursales.html')
def pizzas(request):
    return render(request, 'reportada/pizzas.html')
def paquetes(request):
    return render(request, 'reportada/paquetes.html')
def armatupizza(request):
    return render(request, 'reportada/armatupizza.html')
def googlemaps(request):
	return render(request, 'googlemaps/googlemaps.html')
def googlemaps2(request):
	return render(request, 'googlemaps/googlemaps2.html')
def googlemaps3(request):
	return render(request, 'googlemaps/googlemaps3.html')

class RegistroCliente(generic.CreateView):
	model=User
	template_name="accounts/registrar.html"
	form_class = FormRegistro
	success_url = reverse_lazy('reportada_app:sesion')

def sesion(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]
			user=authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, "reportada/index.html")
				
	else:
		form=LoginForm()
	context={ 
		"form": form,
		"message": message,	
	}
	return render(request, "accounts/sesion.html", context)
# def login_view(request):
# 	if request.method=='POST':
# 		form=AuthenticationForm(data=request.POST)
# 		if form.is_valid():
# 			user=form.get_user()
# 			login(request, user)
# 			if 'next' in request.POST:
# 				return redirect(request.POST.get('next'))
# 			else:
# 				return redirect('reportada_app:index')
# 		else:
# 			form=AuthenticationForm()
# 		return render(request, 'reportada/index.html', {'form':form})
