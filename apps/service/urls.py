from django.urls import path
from .views import servicesView

urlpatterns = [
    path('', servicesView, name='services'),
]