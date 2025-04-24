from django.urls import path
from .views import *


urlpatterns = [
    path('', main_dashboard, name='main_dahsboard')
]