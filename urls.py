# netbox_plugin_auvik/urls.py

from django.urls import path
from . import views

app_name = 'netbox_plugin_auvik'

urlpatterns = [
    path('device/<int:pk>/status/', views.device_status_view, name='device_status'),
]
