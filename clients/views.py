from django.contrib.auth.mixins import LoginRequiredMixin #New
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client
from .models import Vehicle
from .models import ServiceRecord
from django.urls import reverse_lazy

class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'

class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    fields = ('client_fname', 'client_lname', 'client_cell_phone', 'client_email', 'client_address_line_1',
              'client_address_line_2', 'client_address_city', 'client_address_state', 'client_address_zip')
    template_name = 'client_edit.html'

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin,CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('client_fname', 'client_lname', 'client_cell_phone', 'client_email', 'client_address_line_1',
              'client_address_line_2', 'client_address_city', 'client_address_state', 'client_address_zip')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('vehicle_vin', 'vehicle_year', 'vehicle_make', 'vehicle_model', 'vehicle_owner')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('client_list')


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ('vehicle_vin', 'vehicle_year', 'vehicle_make', 'vehicle_model', 'vehicle_owner')
    template_name = 'vehicle_edit.html'

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'

class ServiceRecordCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRecord
    template_name = 'servicerecord_new.html'
    fields = ('vehicle_owner', 'service_vehicle', 'service_amount', 'service_details')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ServiceRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRecord
    template_name = 'servicerecord_delete.html'
    success_url = reverse_lazy('vehicle_detail.html')


class ServiceRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRecord
    fields = ('vehicle_owner', 'service_vehicle', 'service_amount', 'service_details')
    template_name = 'servicerecord_edit.html'