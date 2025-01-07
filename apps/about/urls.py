from django.urls import path
from .views import AboutView

urlpatterns = [
    path('', AboutView, name='about'),
]