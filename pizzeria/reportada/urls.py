#from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from django.contrib import admin
from django.contrib.auth import views as auth_views

from reportada import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import url
from reportada.views import *


app_name = "reportada_app"

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^sesion/$', views.sesion, name='sesion'),
    url(r'^sucursales/$', views.sucursales, name='sucursales'),
    url(r'^paquetes/$', views.paquetes, name='paquetes'),
    url(r'^pizzas/$', views.pizzas, name='pizzas'),
    url(r'^armatupizza/$', views.armatupizza, name='armatupizza'),
    url(r'^googlemaps/$', views.googlemaps, name='googlemaps'),
    url(r'^googlemaps2/$', views.googlemaps2, name='googlemaps2'),
    url(r'^googlemaps3/$', views.googlemaps2, name='googlemaps3'),
	url(r'^registrar/$', views.RegistroCliente.as_view(), name='registrar'),
	url(r'^logout/$', LogoutView.as_view(), {"next_page": settings.LOGOUT_REDIRECT_URL}, name="logout"),

]