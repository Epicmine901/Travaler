from django.urls import path
from .views import packagesView

urlpatterns = [
    path('', packagesView, name='packages'),
]