from .models import Client
from .models import Vehicle
from django import forms
from django.contrib.auth.forms import forms

class ClientCreationForm(forms.Form):
    class Meta:
        model = Client
        fields = ('client_fname', 'client_lname', 'client_cell_phone', 'client_email', 'client_address_line_1',
                  'client_address_line_2', 'client_address_city', 'client_address_state', 'client_address_zip')

class VehicleCreationForm(forms.Form):
    model = Vehicle
    fields = ('vehicle_vin', "vehicle_make")

