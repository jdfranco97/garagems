from .models import Client
from django import forms
from django.contrib.auth.forms import forms

class ClientCreationForm(forms.Form):
    model = Client
    fields = ('client_fname')

