from django.urls import path

from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    VehicleCreateView,
    VehicleDeleteView,
    VehicleUpdateView,
    VehicleDetailView,
    ServiceRecordCreateView,
    ServiceRecordDeleteView,
    ServiceRecordUpdateView,
)



urlpatterns = [
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/vehicle/', VehicleCreateView.as_view(), name='vehicle_new'),
    path('<int:pk>/vehicle/delete/',
         VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('<int:pk>/vehicle/edit/',
         VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('<int:pk>/vehicle/detail',
         VehicleDetailView.as_view(), name='vehicle_detail'),
    path('new/vehicle/servicerecord', ServiceRecordCreateView.as_view(), name='servicerecord_new'),
    path('<int:pk>/vehicle/servicerecord/delete/',
         ServiceRecordDeleteView.as_view(), name='servicerecord_delete'),
    path('<int:pk>/vehicle/servicerecord/edit/',
         ServiceRecordUpdateView.as_view(), name='servicerecord_edit'),
]