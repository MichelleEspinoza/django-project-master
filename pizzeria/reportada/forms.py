from django import forms
from django.db import models
from .models import Registro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormRegistro(UserCreationForm):
	first_name=forms.CharField(widget=forms.TextInput())
	last_name=forms.CharField(widget=forms.TextInput())
	email= forms.CharField(widget=forms.EmailInput())
	username= forms.CharField(widget=forms.TextInput())
	password1=forms.CharField(widget=forms.PasswordInput())
	password2=forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model=User
		fields=[
		"first_name",
		"last_name",
		"email",
		"username",
		"password1",
		"password2"
	]

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())
