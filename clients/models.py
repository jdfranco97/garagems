from django.db import models
import random
# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


def random_string():
    return str(random.randint(1000000000, 9999999999))

class Client(models.Model):
    client_fname = models.CharField ("First Name", max_length=50, default=' ', null=True, blank=False,)
    client_lname = models.CharField("Last Name",max_length=50, default=' ', null=True, blank=False)
    client_cell_phone = models.CharField ("Cell Phone",max_length=50, default=' ', null=True, blank=False)
    client_email = models.EmailField("Email",max_length=100, default=' ')
    client_address_line_1 = models.CharField("Address Line 1",max_length=50, default=' ', null=True, blank=True)
    client_address_line_2 = models.CharField("Address Line 2",max_length=50, default=' ', null=True, blank=True)
    client_address_city = models.CharField("City",max_length=50, default=' ', null=True, blank=True)
    client_address_state = models.CharField("State",max_length=50, default=' ', null=True, blank=True)
    client_address_zip = models.CharField("Zip",max_length=50, default=' ', null=True, blank=True)
    acct_number = models.CharField("Account Number",max_length=50,blank=False, null=True, default = random_string)
    notes = models.TextField()
    date = models.DateTimeField("Date",auto_now_add=True)

    def __str__(self):
        return self.client_fname

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])

class Vehicle(models.Model):
    vehicle_owner = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='vehicles',
    )
    vehicle_vin = models.CharField("VIN Number", max_length=140)
    vehicle_year = models.CharField("Year", max_length=4, blank=False)
    vehicle_make = models.CharField("Make", max_length=50, blank=False)
    vehicle_model = models.CharField("Model", max_length=50, blank=False)

    def __str__(self):
        return self.vehicle_vin

    def get_absolute_url(self):
        return reverse('client_list')

class ServiceRecord(models.Model):
    vehicle_owner = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='vehicle_owner',
    )
    service_vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='servicerecords',
    )
    service_date = models.DateTimeField("Date",auto_now_add=True)
    service_amount = models.CharField("Amount", max_length=4, blank=False)
    service_details = models.CharField("Service Details", max_length=140)

    def __str__(self):
         return self.service_details

    def get_absolute_url(self):
        return reverse('Client_list')